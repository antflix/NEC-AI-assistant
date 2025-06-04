
import logging
from math import log
import os
import re
import time
import json
from typing import Any, List
from helper_functions import *
import pandas as pd
from langchain.chains import LLMChain
# from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from langchain.chains.qa_with_sources.retrieval import \
    RetrievalQAWithSourcesChain
from langchain.docstore.document import Document
from langchain.prompts import PromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.retrievers import BaseRetriever
from langchain_ollama import ChatOllama
from sentence_transformers import CrossEncoder

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

path = "./static/csv/NEC_url.csv"
save_path = "./static/indexes/faiss_index-html"
def log_method_name(func):
    def wrapper(*args, **kwargs):
        current_method_name = func.__name__
        print(f"Current method name: {current_method_name}")
        return func(*args, **kwargs)
    return wrapper
# Modify the get_relevant_documents method to include table insertion
class CrossEncoderRetriever(BaseRetriever):
    vectorstore: Any
    cross_encoder: Any
    k: int = 5
    rerank_top_k: int = 3
    
    @log_method_name
    def get_relevant_documents(self, query: str) -> List[Document]:
        logging.info("Starting initial retrieval")
        start_time = time.time()

        # Initial retrieval
        initial_docs = self.vectorstore.similarity_search(query, k=self.k)

        logging.info(f"Initial retrieval completed in {time.time() - start_time} seconds")

        logging.info("Starting cross-encoder reranking")
        start_time = time.time()

        # Prepare pairs for cross-encoder
        pairs = [[query, doc.page_content] for doc in initial_docs]

        # Get cross-encoder scores
        scores = self.cross_encoder.predict(pairs)

        # Sort documents by score
        scored_docs = sorted(zip(initial_docs, scores), key=lambda x: x[1], reverse=True)

        logging.info(f"Cross-encoder reranking completed in {time.time() - start_time} seconds")

        # Load the table dictionary
        table_dict_path = './static/json/combined_tables.json'
        table_dict = load_dict_from_json(table_dict_path)

        # Insert tables into documents
        updated_docs = []
        for doc, _ in scored_docs[:self.rerank_top_k]:
            doc.page_content = find_and_insert_tables(doc.page_content, table_dict)
            updated_docs.append(doc)

        # Return top reranked documents with inserted tables
        return updated_docs

    @log_method_name
    async def aget_relevant_documents(self, query: str) -> List[Document]:
        raise NotImplementedError("Async retrieval not implemented")
    
@log_method_name
def encode_csv(path, chunk_size=1000, chunk_overlap=200, save_path="faiss_index"):
    """
    Encodes a CSV file into a vector store using OpenAI embeddings and saves the vector store to disk.

    Args:
        path: The path to the CSV file.
        chunk_size: The desired size of each text chunk.
        chunk_overlap: The amount of overlap between consecutive chunks.
        save_path: The directory path where the FAISS index will be saved.

    Returns:
        A FAISS vector store containing the encoded CSV content.
    """
    start_time = time.time()
    logging.info("Loading CSV data")

    # Load CSV data
    df = pd.read_csv(path)
    logging.info("CSV data loaded successfully")

    # Check if required columns exist in the dataframe
    required_columns = ['Chapter', 'Reference', 'URL', 'Body']
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Column '{col}' not found in CSV")

    logging.info("Processing documents")
    documents = []
    for _, row in df.iterrows():
        doc = Document(
            page_content=row['Body'],
            metadata={
                'Chapter': row['Chapter'],
                'Reference': row['Reference'],
                'URL': row['URL']
            }
        )
        documents.append(doc)

    logging.info("Splitting documents into chunks")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap, length_function=len
    )
    texts = text_splitter.split_documents(documents)
    cleaned_texts = replace_t_with_space(texts)

    logging.info("Creating embeddings and vector store")
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(cleaned_texts, embeddings)

    # Save the FAISS index to disk
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    logging.info("Saving FAISS index to disk")
    vectorstore.save_local(save_path)
    logging.info(f"FAISS index saved successfully in {save_path}")

    end_time = time.time()
    logging.info(f"Encoding CSV completed in {end_time - start_time} seconds")

    return vectorstore
import faiss
import os
import logging
from langchain_community.vectorstores import FAISS # Adjust import based on your setup

res = faiss.StandardGpuResources()

@log_method_name
def load_vector_store(save_path):
    """
    Loads a FAISS vector store from disk if it exists and transfers it to the GPU.

    Args:
        save_path: The directory path where the FAISS index is saved.

    Returns:
        A FAISS vector store loaded from disk and transferred to GPU, or None if the index does not exist.
    """
    if os.path.exists(save_path) and os.path.isdir(save_path):
        try:
            # Load the vector store
            vectorstore = FAISS.load_local(save_path, OpenAIEmbeddings(), allow_dangerous_deserialization=True)
            
            # Extract the FAISS index from the vector store
            faiss_index = vectorstore.index
            
            # Transfer the FAISS index to the GPU
            gpu_index = faiss.index_cpu_to_gpu(res, 0, faiss_index)  # 0 is the GPU id
            
            # Replace the original index with the GPU index
            vectorstore.index = gpu_index
            
            logging.info(f"FAISS index loaded and transferred to GPU successfully from {save_path}")
            return vectorstore
        except Exception as e:
            logging.error(f"Failed to load FAISS index from {save_path}: {e}")
            return None
    else:
        logging.info(f"FAISS index not found at {save_path}")
        return None
    
@log_method_name
# Load the tables dictionary from JSON
def load_dict_from_json(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)


@log_method_name
# Helper function to find and insert tables
def find_and_insert_tables(doc_content, table_dict):
    pattern = r"Table\s+\d+(\.\d+)*(\([A-Za-z\d]+\))*"  # Updated regex pattern to match complex table references
    matches = re.finditer(pattern, doc_content)
    print(f"FOUND TABLE: {matches}")
    for match in matches:
        table_ref = match.group()
        table_html = table_dict.get(table_ref)

        if table_html:
            insert_position = match.end()  # Insert directly after the match
            doc_content = (
                doc_content[:insert_position]
                + "\n\n"  # Ensure it is on a new line
                + table_html
                + "\n\n"
                + doc_content[insert_position:]
            )

    return doc_content


# Load or create the vector store and other components as done in your existing code
vectorstore = load_vector_store(save_path)
if vectorstore is None:
    vectorstore = encode_csv(path, save_path=save_path)

cross_encoder = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')

cross_encoder_retriever = CrossEncoderRetriever(
    vectorstore=vectorstore,
    cross_encoder=cross_encoder,
    k=10,  # Retrieve 10 documents initially
    rerank_top_k=5  # Return top 5 after reranking
)

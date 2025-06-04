import json
import logging
import os
import re
import sys
import time
from typing import Any, List
from langchain.memory import ConversationSummaryBufferMemory
from langchain_ollama import ChatOllama
import pandas as pd
import spacy
from flask import Flask, jsonify, render_template, request
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
#   from sympy import enable_warnings
import torch
from transformers import BertTokenizer, BertForSequenceClassification
from conduit_fill_query import *
from helper_functions import *
# from NEC_query import handle_nec_query
from vector import *
import inspect




# Initialize the Flask application
app = Flask(__name__)
def log_method_name(func):
    def wrapper(*args, **kwargs):
        current_method_name = func.__name__
        print(f"Current method name: {current_method_name}")
        return func(*args, **kwargs)
    return wrapper

# Load the BERT model and tokenizer
model_path = "./static/models/classification_Model"
tokenizer = BertTokenizer.from_pretrained(model_path)
model = BertForSequenceClassification.from_pretrained(model_path)

# Load your SpaCy classification model

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
os.environ["OPENAI_API_KEY"] = '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'

from langchain.memory import ConversationSummaryBufferMemory
from langchain_openai import OpenAI# Set up the memory
llm = OpenAI(
	temperature=0,
	openai_api_key="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",
	model_name="asst_xn9bJhPFcfZwxj7gNvTXDsFs"
)
# memory = ConversationSummaryBufferMemory(llm=llms, input_key="input", max_token_limit=4000)
# Set up the LLM and QA chain

# llm = ChatOllama(model="NECllama3_2_1B", temperature=0.7)

# from langchain_community.llms.llamafile import Llamafile
# llm = Llamafile()
# llm = OpenAI(
# 	temperature=0,
# 	openai_api_key="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",
# 	model_name="gpt-4o-mini"
# )
# from langchain_openai import ChatOpenAI
# llm = ChatOpenAI(
#         openai_api_base="http://10.0.1.21:8000/v1",
#         openai_api_key="dummy_value",
#         model_name="anthonymeo/full-train-openai")



# Initialize ConversationSummaryBufferMemory
# memory = ConversationSummaryBufferMemory(llm=llm, input_key="input", max_token_limit=1000)
# NEC prompt template
nec_prompt_template = PromptTemplate(
    input_variables=["question", "context"],
    template="""
System: You are an expert assistant helping to answer questions based on the National Electrical Code (NEC) and other relevant sources.
        Please provide accurate and detailed answers, including any relevant citations and source links to the URL provided for each Document.

User: {question}

Context: {context}



Assistant:
    """
)
# Conduit-fill prompt template
conduit_fill_prompt_template = PromptTemplate(
    input_variables=["question", "context", "calculated_answer", "conduit_type", "conduit_size", "conductor_type", "conductor_size", "conductor_area", "conduit_fill_capacity"],
    template="""
System: You are an expert assistant specializing in conduit fill calculations and related queries.
        Please provide accurate and detailed answers, include all URLs provided in the below context in markdown format.
        When referencing the information in the context do not mention the word "context" or "information you provided". Only reference the URLs and tables themselves.
        Please wrap all calculations in double $$ signs and write the equations in LaTeX notations.
        Think through the entire problem and come up with a complete solution.
        Explain each step in detail, numbering the steps as you explain each detail in your response.
        Use an asterisk * when including details under each numbered step so as to make your response more readable.
        List the User Provided details in a bulleted list at the beginning of your response.
        List the Conductor and Conduit details in a bulleted list, citing the URL link to the tables as sources.
        Write out the calculations with an explination of each step.
        State the final answer in a clear and concise sentence.
        
User: {question}

Context: {context}



Assistant:
"""
)
# Conduit-fill prompt template
conduit_fill_no_conduit_size_prompt_template = PromptTemplate(
    input_variables=["question", "context", "conduit_type", "conduit_size"],
    template="""
System:You are an expert assistant specializing in conduit fill calculations and related queries.
        Please provide accurate and detailed answers, include all URLs provided in the below context in markdown format.
        When referencing the information in the context do not mention the word "context" or "information you provided". Only reference the URLs and tables themselves.
        Please wrap all calculations in double $$ signs and write the equations in LaTeX notations.
        Think through the entire problem and come up with a complete solution.
        Explain each step in detail, numbering the steps as you explain each detail in your response.
        Use an asterisk * when including details under each numbered step so as to make your response more readable.
        List the User Provided details in a bulleted list at the beginning of your response.
        List the Conductor and Conduit details in a bulleted list, citing the URL link to the tables as sources.
        Write out the calculations with an explination of each step.
        State the final answer in a clear and concise sentence.
        

User: {question}

Context: {context}


Assistant:
    """
)
missing_info_prompt_template = PromptTemplate(
    input_variables=["question", "conduit_type", "conduit_size", "conductor_type", "conductor_size", "num_conductors", "missing_info"],
    template="""
    You are a helpful assistant who assists users in performing conduit fill calculations. 
    If the user hasn't provided all the required information, do the following:

    1. Politely ask the user to provide the missing details.
    2. Clearly specify what information is required for the calculation:
    3. If some information has been provided, acknowledge what has been given.
    4. Maintain a friendly and helpful tone, ensuring that the user knows you're here to assist them in completing the calculation.


    - Conduit Type: {conduit_type}
    - Conductor Type: {conductor_type}
    - Conductor Size: {conductor_size}
    - Conduit Size: {conduit_size}
    - Number of Conductors: {num_conductors}

    To proceed, kindly ask the user to restate the question and provide:
    {missing_info}
    """
) 


#
# Combined preprocessing and prediction function
@log_method_name
def classify_query(query):
    # Tokenize and preprocess the input query
    inputs = tokenizer(query, padding=True, truncation=True, return_tensors="pt")
    # Ensure the model is in evaluation mode
    model.eval()
    # Disable gradient calculation for inference
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        prediction_idx = torch.argmax(logits, dim=-1).cpu().item()
    # Map the prediction to the corresponding label
    labels = ["nec", "conduit_fill"]  # Adjust these labels based on your actual model configuration
    return labels[prediction_idx]


@log_method_name
def run_qa_chain(llm, query, context, prompt_template):
    # Create the LLMChain with the provided prompt template
    qa_llm_chain = LLMChain(
        llm=llm,
        prompt=prompt_template,
    )
    
    # Create the StuffDocumentsChain
    stuff_documents_chain = StuffDocumentsChain(
        llm_chain=qa_llm_chain,
        document_variable_name="context",
    )
    
    # Create the final QA chain
    qa_chain = RetrievalQAWithSourcesChain(
        retriever=cross_encoder_retriever,
        combine_documents_chain=stuff_documents_chain,
        return_source_documents=True
    )
    
    # Use the `_call` method to get all outputs
    result = qa_chain({"question": query, "context": context})
    
    # Access specific keys from the result
    answer = result.get('answer')
    source_documents = result.get('source_documents')

    return {
        "answer": answer,
        "source_documents": source_documents
    }


@log_method_name
def handle_nec_query(query):
    logging.info(f"Handling NEC query: {query}")
    
    # Run a similarity search to retrieve relevant context documents
    context_docs = cross_encoder_retriever.get_relevant_documents(query)
    
    # Extract the content from the retrieved documents
    context = "\n\n".join([doc.page_content for doc in context_docs])

    # Prepare metadata for each document
    documents = []
    for doc in context_docs:
        documents.append({
            "content": doc.page_content,
            "chapter": doc.metadata['Chapter'],
            "reference": doc.metadata['Reference'],
            "url": doc.metadata['URL']
        })

    return context, documents


@log_method_name
def run_conduit_fill_chain(llm, query, context, prompt_template):
    logging.debug(f"Running LLM Chain with context: {context} and query: {query}")
    
    llm_chain = LLMChain(
        llm=llm,
        prompt=prompt_template,
    )
    
    result = llm_chain.apply([{"question": query, "context": context}])
    
    logging.debug(f"LLM Chain Result: {result}")

    if result and isinstance(result, list) and len(result) > 0:
        answer = result[0].get('text')  # Ensure 'text' is the correct key
    else:
        answer = None
    
    return {
        "answer": answer,
        "context": context  # Ensure context is returned
    }
    
    
@log_method_name
def handle_missing_info_query(llm, query, entities, prompt_template):
    logging.info("Handling query with missing information.")
    missing_info = []

    # Check for missing information and append to missing_info list
    if not entities.get("conduit_type"):
        missing_info.append("The type of conduit (e.g., EMT, PVC)")
    if not entities.get("conductor_type"):
        missing_info.append("The type of conductors being used (e.g., THHN, THWN)")
    if not entities.get("conductor_size"):
        missing_info.append("The size of the conductors (e.g., #12, #10, #1/0)")
    if not entities.get("conduit_size"):
        missing_info.append("The size of the conduit (e.g., 1/2 inch, 3/4 inch, 1 inch, ...)")
    if not entities.get("num_conductors"):
        missing_info.append("The number of conductors being used")

    # Create context to display both provided and missing information
    context = f"""
    Here's the information you provided:
    - Conduit Type: {entities.get("conduit_type", "Not provided")}
    - Conductor Type: {entities.get("conductor_type", "Not provided")}
    - Conductor Size: {entities.get("conductor_size", "Not provided")}
    - Conduit Size: {entities.get("conduit_size", "Not provided")}
    - Number of Conductors: {entities.get("num_conductors", "Not provided")}

    Missing information: {'; '.join(missing_info) if missing_info else 'None'}
    """

    # Preprocess the input variables for the prompt
    input_variables = {
        "question": query,
        "context": context,
        "conduit_type": entities.get("conduit_type", "Not provided yet"),
        "conduit_size": entities.get("conduit_size", "Not provided yet"),
        "conductor_type": entities.get("conductor_type", "Not provided yet"),
        "conductor_size": entities.get("conductor_size", "Not provided yet"),
        "num_conductors": entities.get("num_conductors", "Not provided yet"),
        "missing_info": "\n".join(missing_info)
    }

    llm_chain = LLMChain(
        llm=llm,
        prompt=prompt_template,
    )
    
    result = llm_chain.apply([input_variables])
    
    if result and isinstance(result, list) and len(result) > 0:
        answer = result[0].get('text')  # Ensure 'text' is the correct key
    else:
        answer = "It seems like I couldn't generate a response. Please try again with more details."
    
    return {
        "answer": answer,
        "context": context
    }
@app.route('/query', methods=['POST'])
def query():
    from conduit_fill_query import extract_entities
    logging.info("Handling query...")
    
    data = request.json
    query = data.get('query')
    
    if not query:
        logging.error("No query provided.")
        return jsonify({"error": "No query provided"}), 400

    logging.info(f"Received query: {query}")

    category = classify_query(query)
    logging.info(f"Classified query as category: {category}")
    
    table_html = ""
    documents = []  # Initialize documents as an empty list
    
    # Load the previous conversation memory
    # memory.load_memory_variables({"question": query})

    if category == "nec":
        context, documents = handle_nec_query(query)
        prompt_template = nec_prompt_template
        result = run_qa_chain(llm, query, context, prompt_template)
        # Save context and result after obtaining the result
        combined_input = f"Context: {context}\nQuestion: {query}"
        # memory.save_context({"input": combined_input}, {"answer": result['answer']})

    elif category == "conduit_fill":
        entities = extract_entities(query)
        
        if entities.get("conduit_type") and entities.get("conductor_type") and entities.get("conductor_size"):
            if entities.get("num_conductors"):
                result = handle_query_with_num_conductors(
                    llm, query, entities, conduit_fill_no_conduit_size_prompt_template
                )
            elif entities.get("conduit_size"):
                result = handle_query_with_conduit_size(
                    llm, query, entities, conduit_fill_prompt_template
                )
            else:
                result = handle_missing_info_query(llm, query, entities, missing_info_prompt_template)
                
        else:
            # Handle missing info if any required data is not provided
            result = handle_missing_info_query(llm, query, entities, missing_info_prompt_template)
        
        context = result['context']
        documents = [context]
        combined_input = f"Context: {context}\nQuestion: {query}"
        # memory.save_context({"input": combined_input}, {"answer": result['answer']})
        
        # Initialize tables as empty strings to avoid issues with undefined variables
        conduit_table_html = ""
        conductor_table_html = ""



        if entities.get("conduit_type") != 'Not provided' and entities.get("conductor_type") != 'Not provided':
            # Find the tables only if both conduit_type and conductor_type are provided
            conduit_table_html, conductor_table_html = find_table_html(entities.get("conductor_type"), entities.get("conduit_type"))



            # Highlight the tables only if the result has the necessary values
            if 'conduit_result' in result and 'Fill Capacity (in²)' in result['conduit_result']:
                conduit_table_html = highlight_table(conduit_table_html, result['conduit_result']['Fill Capacity (in²)'])
            if 'conductor_result' in result and 'Approximate Area (in²)' in result['conductor_result']:
                conductor_table_html = highlight_table(conductor_table_html, result['conductor_result']['Approximate Area (in²)'])
        
        # Construct the table HTML with fallback or placeholder values
        table_html = f"""
        <a href="https://2023.antflix.net#table_4({entities.get("conduit_type", "N/A")})" style="color: lightblue; text-decoration: underline; size: 18px;">Chapter 9- Table 4</a>\n
        {conduit_table_html if conduit_table_html else '<p>No conduit table available</p>'}
        \n\n\n
        <a href="https://2023.antflix.net#table_5({entities.get("conductor_type", "N/A")})" style="color: lightblue; text-decoration: underline; size: 18px;">Chapter 9- Table 5</a>\n
        {conductor_table_html if conductor_table_html else '<p>No conductor table available</p>'}
        """
    else:
        logging.error("Unknown classification category.")
        return jsonify({"error": "Unknown classification category"}), 400
    print(f"Result: {result}")
    return jsonify({
        "answer": result['answer'],
        "context": context,
        "documents": documents,
        "category": category,
        "table_html": table_html
    })
    
    
    
# @app.route('/get_memory', methods=['GET'])
# def get_memory():
#     memory_variables = memory.load_memory_variables({})
#     return jsonify({"memory": memory_variables})

def highlight_table(table_html, target_value):
    target_value_str = str(target_value)
    
    # Debugging: Print the value being searched for
    print(f"Searching for value: {target_value_str}")

    # Use regex to find the exact cell containing the target value and add the highlight class
    highlighted_table_html = re.sub(
        f'(<td[^>]*>\\s*){target_value_str}(\\s*</td>)',
        f'\\1<span class="highlight">{target_value_str}</span>\\2',
        table_html
    )

    if target_value_str in highlighted_table_html:
        print(f"Value {target_value_str} found and highlighted.")
    else:
        print(f"Value {target_value_str} not found in table.")

    return highlighted_table_html
    
    
    
def load_table_data():
    # Load the JSON data for conduit and conductor tables
    with open('./static/json/table4.json', 'r') as f4, open('./static/json/table5.json', 'r') as f5:
        table4_data = json.load(f4)
        table5_data = json.load(f5)
    return table4_data, table5_data

def find_table_html(conductor_type, conduit_type):
    table4_data, table5_data = load_table_data()

    if conductor_type is None:
        conductor_table_html = "Conductor type not provided."
    else:
        # Safeguard against None by using a default value or a check before calling upper()
        conductor_table_html = table5_data.get(conductor_type.upper(), "No table found for conductor type.")
    
    if conduit_type is None:
        conduit_table_html = "Conduit type not provided."
    else:
        conduit_table_html = table4_data.get(conduit_type.upper(), "No table found for conduit type.")

    return conductor_table_html, conduit_table_html




@log_method_name
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        question = request.form['question']
        logging.info(f"Received question: {question}")

        # Use the same logic as the /query route
        from conduit_fill_query import extract_entities
        
        category = classify_query(question)
        logging.info(f"Classified question as category: {category}")

        if category == "nec":
            context = handle_nec_query(question)
            prompt_template = nec_prompt_template
            result = run_qa_chain(llm, question, context, prompt_template)
            table_html = ""
        elif category == "conduit_fill":
            context, conductor_result, conduit_result = handle_conduit_fill_query(question)
            prompt_template = conduit_fill_prompt_template
            result = run_conduit_fill_chain(llm, question, context, prompt_template)
            
            if not isinstance(context, list):
                context = [context]  # Ensure context is an array

            entities = extract_entities(question)
            conduit_type = entities.get('conduit_type')
            conductor_type = entities.get('conductor_type')

            logging.info(f"Extracted entities - Conduit Type: {conduit_type}, Conductor Type: {conductor_type}")

            conduit_table_html, conductor_table_html = find_table_html(conductor_type, conduit_type)
            
            # Highlight the values in the tables
            conduit_table_html = highlight_table(conduit_table_html, conduit_result['Fill Capacity (in²)'])
            conductor_table_html = highlight_table(conductor_table_html, conductor_result['Approximate Area (in²)'])
            
            table_html = f"""
            <a href="https://2023.antflix.net#table_4({conduit_type})" style="color: lightblue; text-decoration: underline; size: 18px;">Chapter 9- Table 4</a>\n
            {conduit_table_html}
            \n\n\n
            <a href="https://2023.antflix.net#table_5({conductor_type})" style="color: lightblue; text-decoration: underline; size: 18px;">Chapter 9- Table 5</a>\n
            {conductor_table_html}
            """
        else:
            return jsonify({"error": "Unknown classification category"}), 400

        return jsonify({
            "answer": result['answer'],
            "documents": context,
            "category": category,
            "table_html": table_html
        })
    return render_template('index.html')


# @app.route('/clear_memory', methods=['POST'])
# def clear_memory():
#     memory.clear()  # This clears the stored memory
#     return jsonify({"message": "Memory cleared"})

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=6005)
    
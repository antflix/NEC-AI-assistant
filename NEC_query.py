# handle_nec.py
from flask import jsonify
import logging
def log_method_name(func):
    def wrapper(*args, **kwargs):
        current_method_name = func.__name__
        print(f"Current method name: {current_method_name}")
        return func(*args, **kwargs)
    return wrapper






# Function to handle NEC queries
@log_method_name
def handle_nec_query(query, qa_chain):
    logging.info(f"Handling NEC query: {query}")
    
    # Run the QA chain
    result = qa_chain({"question": query})

    # Prepare the response
    answer = result['answer']
    source_documents = result['source_documents']
    
    documents = []
    for doc in source_documents:
        documents.append({
            "content": doc.page_content,
            "chapter": doc.metadata['Chapter'],
            "reference": doc.metadata['Reference'],
            "url": doc.metadata['URL']
        })

    return {"answer": answer, "documents": documents}
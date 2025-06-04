import json
import logging
from click import prompt
from functools import wraps
import spacy
import math

from torch import fill_

# Load your NER model
nlp = spacy.load("./static/models/conduit_fill_ner_model")


# Paths to the .json files containing constants
CONDUITS_JSON_PATH = "./static/json/Chapter_9-Table_4.json"
CONDUCTORS_JSON_PATH = "./static/json/Chapter_9-Table_5.json"
def log_method_name(func):
    def wrapper(*args, **kwargs):
        current_method_name = func.__name__
        print(f"Current method name: {current_method_name}")
        return func(*args, **kwargs)
    return wrapper

  
@log_method_name
def handle_conduit_fill_query(query):
    """Main entry point for conduit fill calculations
    
    Architecture Flow:
    ```mermaid
    graph TD
        A[app.py] -->|imports via *| B[handle_conduit_fill_query]
        B -->|calls| C[extract_entities]
        B -->|routes to| D[handle_query_with_conduit_size]
        B -->|routes to| E[handle_query_with_num_conductors]
        D -->|uses| F[LLMChain from app.py]
    ```
    """
    from app import handle_missing_info_query
    entities = extract_entities(query)
    if entities.get("conduit_size"):
        return handle_query_with_conduit_size(query, entities)
    elif entities.get("num_conductors"):
        return handle_query_with_num_conductors(query, entities)
    else:
        return handle_missing_info_query(query, entities)

# Function to load the conduit constants from the JSON file
@log_method_name
def load_conduits():
    with open(CONDUITS_JSON_PATH, 'r') as f:
        return json.load(f)
    
    
    
# Function to load the conductor constants from the JSON file
@log_method_name
def load_conductors():
    with open(CONDUCTORS_JSON_PATH, 'r') as f:
        return json.load(f)



@log_method_name
def extract_entities(query_text):
    doc = nlp(query_text)
    entities = {
        "conduit_type": None,
        "conduit_size": None,
        "conductor_type": None,
        "conductor_size": None,
        "num_conductors": None
    }
    for ent in doc.ents:
        if ent.label_ == "CONDUIT_TYPE":
            entities["conduit_type"] = ent.text
        elif ent.label_ == "CONDUIT_SIZE":
            entities["conduit_size"] = ent.text
        elif ent.label_ == "CONDUCTOR_TYPE":
            entities["conductor_type"] = ent.text
        elif ent.label_ == "CONDUCTOR_SIZE":
            entities["conductor_size"] = ent.text
        elif ent.label_ == "NUM_CONDUCTORS":
            entities["num_conductors"] = ent.text
        logging.info(f"Extracted entity: {ent.text}, Label: {ent.label_}")
    
    logging.info(f"Final entities: {entities}")
    return entities




@log_method_name
def search_conductor_type_and_size(conductor_type, conductor_size, conductors):
    conductor_type = conductor_type.upper()
    conductor_size = conductor_size.upper()

    # Check if conductors is a list
    if not isinstance(conductors, list):
        logging.error("Conductors data is not a list.")
        return None
    
    for entry in conductors:
        # Check if entry is a dictionary
        if not isinstance(entry, dict):
            logging.error(f"Entry is not a dictionary: {entry}")
            continue
        
        # Debugging: print the entry
        logging.debug(f"Checking entry: {entry}")
        
        if conductor_type in entry['Type'].upper() and entry['Size'].upper() == conductor_size:
            logging.info(f"Match for conductor type: {conductor_type} and size: {conductor_size} in {entry['Size']}")
            return {
                "Type": entry['Type'],
                "Size": conductor_size,
                "Approximate Area (in²)": entry['Approximate Area (in²)'],
                "URL": entry['URL']
            }
    return None




@log_method_name
def handle_query_with_num_conductors(llm, query, entities, prompt_template):
    from app import LLMChain
    logging.info("Handling query with provided number of conductors.")
    
    # Load the constants from the JSON files
    conductors = load_conductors()
    conduits = load_conduits()
    
    # Search for the conductor details
    conductor_result = search_conductor_type_and_size(entities["conductor_type"], entities["conductor_size"], conductors)
    
    # Estimate conduit size based on the number of conductors
    conduit_result, previous_conduit, next_conduit = estimate_conduit_size(entities["conduit_type"], conductor_result, entities["num_conductors"], conduits)
    
    # Build the context string
    context, fill_percentage = build_conduit_context_with_num_conductors(conductor_result, conduit_result, previous_conduit, next_conduit, entities["num_conductors"])

    # Prepare the input for the prompt template
    input_variables = {
        "question": query,
        "context": context,
        "conduit_type": entities.get("conduit_type", "Not provided"),
        "conduit_size": entities.get("conduit_size", "Not provided"),
        "conductor_type": entities.get("conductor_type", "Not provided"),
        "conductor_size": entities.get("conductor_size", "Not provided"),
        "num_conductors": entities.get("num_conductors", "Not provided"),
        "fill_percentage": fill_percentage
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
    
    print(prompt_template.format(**input_variables))

    return {
        "answer": answer,
        "context": context,
        "conductor_result": conductor_result,
        "conduit_result": conduit_result
    }
    
def build_conduit_context_with_num_conductors(conductor_result, conduit_result, previous_conduit, next_conduit, num_conductors):
    context = "  \n"
    
    if conductor_result:
        total_area_occupied = float(conductor_result['Approximate Area (in²)']) * int(num_conductors)
        context += f"<u><strong>User Provided Information:</strong></u>  \n"
        context += f"**Conductor Type:** *{conductor_result['Type']}*  \n"
        context += f"**Conductor Size:** *{conductor_result['Size']}*  \n"
        context += f"**Number of Conductors:** *{num_conductors}*  \n"
        context += f"**Conduit Type:** *{conduit_result['Type']}*  \n  \n"

        context += f"<u><strong>Conductor Information from [Chapter 9 Table 5({conductor_result['Type']})]({conductor_result['URL']}):</strong></u>  \n"
        context += f"**Conductor Area:** *{conductor_result['Approximate Area (in²)']} in²*  \n"
        context += f"**Total Area occupied by conductors:** *{num_conductors} * {conductor_result['Approximate Area (in²)']} in² = {total_area_occupied:.4f} in²*  \n"
        context += f"**Link:** [Chapter 9 Table 5({conductor_result['Type']})]({conductor_result['URL']})  \n  \n"

    if previous_conduit:
        context += f"<u><strong>Conduit Information from [Chapter 9 Table 4({conduit_result['Type']})]({conduit_result['URL']}):</strong></u>  \n"
        context += f"**{previous_conduit['Trade Size']} inch {conduit_result['Type']}:** *{previous_conduit['Fill Capacity (in²)']} in²*  \n"
        
    if conduit_result:
        context += f"**{conduit_result['Trade Size']} inch {conduit_result['Type']}:** *{conduit_result['Fill Capacity (in²)']} in²*  \n"

    if next_conduit:
        context += f"**{next_conduit['Trade Size']} inch {conduit_result['Type']}:** *{next_conduit['Fill Capacity (in²)']} in²*  \n"
    
    context += f"**Link:** [Chapter 9 Table 4({conduit_result['Type']})]({conduit_result['URL']})  \n  \n"

    fill_percentage = (total_area_occupied / conduit_result['Fill Capacity (in²)']) * 100
    context += f"$$\\text{{Space occupied by conductors}} = \\frac{{{total_area_occupied:.4f}}}{{{conduit_result['Fill Capacity (in²)']}}} \\approx {total_area_occupied / conduit_result['Fill Capacity (in²)'] :.2f}$$"
    context += f"**{conduit_result['Trade Size']} inch {conduit_result['Type']} conduit is {fill_percentage:.0f}% full with {num_conductors} {conductor_result['Size']} {conductor_result['Type']} wires**"

    return context, fill_percentage







@log_method_name
def handle_query_with_conduit_size(llm, query, entities, prompt_template):
    from app import LLMChain
    logging.info("Handling query with provided conduit size.")
    
    # Load the constants from the JSON files
    conductors = load_conductors()
    conduits = load_conduits()
    
    # Search for the conductor and conduit details based on extracted entities
    conductor_result = search_conductor_type_and_size(entities["conductor_type"], entities["conductor_size"], conductors)
    conduit_result = search_conduit_type_and_trade_size(entities["conduit_type"], entities["conduit_size"], conduits)
    
    # Build the context and get the calculated max_wires
    context, max_wires = build_conduit_context_with_conduit_size(conductor_result, conduit_result)

    # Prepare the input for the prompt template
    input_variables = {
        "question": query,
        "context": context,
        "calculated_answer": max_wires,  # Include the calculated answer
        "conduit_type": entities.get("conduit_type", "Not provided"),
        "conduit_size": entities.get("conduit_size", "Not provided"),
        "conductor_type": entities.get("conductor_type", "Not provided"),
        "conductor_size": entities.get("conductor_size", "Not provided"),
        "conductor_area": conductor_result['Approximate Area (in²)'] if conductor_result else "Not provided",
        "conduit_fill_capacity": conduit_result['Fill Capacity (in²)'] if conduit_result else "Not provided",
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
    print(prompt_template.format(**input_variables))
    return {
        "answer": answer,
        "context": context,
        "conductor_result": conductor_result,
        "conduit_result": conduit_result
    }
    
    
def build_conduit_context_with_conduit_size(conductor_result, conduit_result):
    context = "  \n"
    
    if conductor_result:
        context += f"<u><strong>User Provided Details:</strong></u>  \n"
        context += f"**Conductor Type:** *{conductor_result['Type']}*  \n"
        context += f"**Conductor Size:** *{conductor_result['Size']}*  \n"
        context += f"**Conduit Type:** *{conduit_result['Type']}*  \n"
        context += f"**Conduit Trade Size:** *{conduit_result['Trade Size']} inch*  \n  \n"
        
        context += f"<u><strong>Conductor Details from Chapter 9 Table 5:</strong></u>  \n"
        context += f"**Conductor Area:** *{conductor_result['Approximate Area (in²)']} in²*  \n"
        context += f"**Link:** [Chapter 9 Table 5({conductor_result['Type']})]({conductor_result['URL']})  \n  \n"

    if conduit_result:
        context += f"<u><strong>Conduit Details from Chapter 9 Table 4:</strong></u>  \n"  # Underlined title for conduit info
        context += f"**Maximum allowable fill capacity (40% of total area):** *{conduit_result['Fill Capacity (in²)']} in²*  \n"
        context += f"**Link:** [Chapter 9 Table 4({conduit_result['Type']})]({conduit_result['URL']})  \n  \n"

    if not conductor_result or not conduit_result:
        context += "!!!!!!!!!!!!!!No matching conductor or conduit data found.!!!!!!!!!!!!!!!!!!!  \n"
    
    max_wires = math.floor(conduit_result['Fill Capacity (in²)'] / conductor_result['Approximate Area (in²)'])
    context += f"$$\\text{{Max number of wires}} = \\frac{{{conduit_result['Fill Capacity (in²)']}}}{{{conductor_result['Approximate Area (in²)']}}} = {conduit_result['Fill Capacity (in²)'] / conductor_result['Approximate Area (in²)']:.2f} \\approx {max_wires}$$"
    
    return context, max_wires



@log_method_name
def estimate_conduit_size(conduit_type, conductor_result, num_conductors, conduits):
    logging.info("Estimating conduit size based on provided conductor information and number of conductors.")
    
    if not conductor_result or not num_conductors:
        logging.error("Cannot estimate conduit size without conductor details and the number of conductors.")
        return None
    
    # Calculate the required fill area for the number of conductors
    required_fill_area = float(conductor_result['Approximate Area (in²)']) * int(num_conductors)
    
    previous_conduit = None
    estimated_conduit = None
    next_conduit = None

    # Find the smallest conduit size that can accommodate the required fill area
    for entry in conduits:
        if entry['Type'].upper().strip() == conduit_type.upper().strip():
            fill_capacity = float(entry['Fill Capacity (in²)'])
            if fill_capacity >= required_fill_area:
                estimated_conduit = {
                    "Type": entry['Type'],
                    "Trade Size": entry['Trade Size'],
                    "Fill Capacity (in²)": fill_capacity,
                    "URL": entry['URL']
                }
                break
            previous_conduit = {
                "Type": entry['Type'],
                "Trade Size": entry['Trade Size'],
                "Fill Capacity (in²)": fill_capacity,
                "URL": entry['URL']
            }
    
    # After the loop, if there's an estimated conduit, try to find the next one
    if estimated_conduit:
        next_conduit_index = conduits.index(entry) + 1
        if next_conduit_index < len(conduits):
            next_entry = conduits[next_conduit_index]
            if next_entry['Type'].upper().strip() == conduit_type.upper().strip():
                next_conduit = {
                    "Type": next_entry['Type'],
                    "Trade Size": next_entry['Trade Size'],
                    "Fill Capacity (in²)": float(next_entry['Fill Capacity (in²)']),
                    "URL": next_entry['URL']
                }
    
    # Logging the results
    logging.info(f"Estimated conduit size: {estimated_conduit['Trade Size']} inch" if estimated_conduit else "No suitable conduit size found.")
    logging.info(f"Previous conduit size: {previous_conduit['Trade Size']} inch" if previous_conduit else "No previous conduit size found.")
    logging.info(f"Next conduit size: {next_conduit['Trade Size']} inch" if next_conduit else "No next conduit size found.")
    
    return estimated_conduit, previous_conduit, next_conduit

@log_method_name
def search_conduit_type_and_trade_size(conduit_type, trade_size, conduits):
    conduit_type = conduit_type.upper().strip()
    trade_size = trade_size.upper().strip()

    # Check if conduits is a list
    if not isinstance(conduits, list):
        logging.error("Conduits data is not a list.")
        return None
    
    for entry in conduits:
        # Check if entry is a dictionary
        if not isinstance(entry, dict):
            logging.error(f"Entry is not a dictionary: {entry}")
            continue
        
        # Debugging: print the entry and the search criteria
        logging.debug(f"Checking entry: {entry}")
        logging.debug(f"Conduit Type: {entry['Type'].upper().strip()}, Trade Size: {entry['Trade Size'].upper().strip()}")
        
        if conduit_type in entry['Type'].upper().strip() and entry['Trade Size'].upper().strip() == trade_size:
            logging.info(f"Match for conduit type: {conduit_type} and trade size: {trade_size} in {entry['Trade Size']}")
            return {
                "Type": entry['Type'],
                "Trade Size": trade_size,
                "Fill Capacity (in²)": entry['Fill Capacity (in²)'],
                "URL": entry['URL']
            }
    logging.info(f"No match found for conduit type: {conduit_type} and trade size: {trade_size}")
    return None

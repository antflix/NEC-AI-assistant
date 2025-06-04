
# # import json
# # import os

# # from flask import Flask, Response, request, stream_with_context
# # from langchain_community.llms import Ollama
# # from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
# # from langchain_core.output_parsers import StrOutputParser

# # # Load environment variables from the .env file

# # app = Flask(__name__)

# # OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://0.0.0.0:11434")
# # OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "NEC_Q4")

# # llm = Ollama(model=OLLAMA_MODEL, base_url=OLLAMA_BASE_URL)

# # prompt = ChatPromptTemplate.from_messages(
# #     [
# #         ("system", "You're a world class assistant"),
# #         MessagesPlaceholder(variable_name="chat_history"),
# #         ("user", "{question}"),
# #     ]
# # )


# # def generate_tokens(question):
# #     chain = prompt | llm | StrOutputParser()
# #     for chunks in chain.stream({"chat_history": [], "question": question}):
# #         yield chunks


# # @app.route("/users/chat", methods=["POST"])
# # def ask_ai():
# #     def generate_json(question):
# #         with app.app_context():  # Ensure we're within the application context
# #             full_content = ""
# #             for token in generate_tokens(question):
# #                 full_content += token
# #                 json_data = {"model": OLLAMA_MODEL, "content": token, "done": False}
# #                 json_str = json.dumps(json_data)  # Convert JSON data to a string
# #                 json_bytes = json_str.encode("utf-8")  # Encode JSON string to bytes
# #                 yield json_bytes
# #                 yield b"\n"  # Yield newline as bytes

# #             # Once streaming is finished, yield one last JSON object with "done" set to True
# #             json_data = {
# #                 "model": OLLAMA_MODEL,
# #                 "full_content": full_content,
# #                 "done": True,
# #             }
# #             json_str = json.dumps(json_data)  # Convert JSON data to a string
# #             json_bytes = json_str.encode("utf-8")  # Encode JSON string to bytes
# #             yield json_bytes

# #     request_data = request.json
# #     question = request_data.get("question")
# #     return Response(
# #         stream_with_context(generate_json(question)), mimetype="application/json"
# #     )


# # if __name__ == "__main__":
# #     app.run(debug=True, host='0.0.0.0', port=6040)


# # import os
# # export ARCEE_API_KEY='42b4974c-0383-4b96-a761-ea66e00f4e90'
# # os.environ['ARCEE_API_URL'] = 'https://app.arcee.ai/api'
# # export ARCEE_ORG='antflix'

# # # Upload CSV
# # import arcee
# # arcee.upload_qa_pairs_from_csv(
# #     qa_set="combine", # The name of the QA set to upload
# #     csv_path="/home/ant/Documents/datasets/train2.csv", # The path to the CSV file containing QA pairs
    
# # )
# # arcee.upload_instructions_from_csv("combined",csv_path="/home/ant/Documents/datasets/train2.csv")

# # export ARCEE_API_KEY='42b4974c-0383-4b96-a761-ea66e00f4e90'

# # arcee.api.upload_hugging_face_dataset_qa_pairs(
# #     "combined",
# #     hf_dataset_id="anthonymeo/combined2",
# #     dataset_split="train",
# #     data_format="chatml"
# # )

# # import arcee
# # arcee.upload_qa_pairs_from_csv(qa_set="combined", csv_path="/home/ant/Documents/datasets/train2.csv")


# # # Environment Setup
# # import os
# # os.environ['ARCEE_API_KEY'] = '42b4974c-0383-4b96-a761-ea66e00f4e90'
# # os.environ['ARCEE_API_URL'] = 'https://app.arcee.ai/api'
# # os.environ['ARCEE_ORG'] = 'antflix'

# # os.environ['HUGGINGFACE_TOKEN'] = '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'

# # # Upload Hugging Face Dataset
# # import arcee
# # arcee.upload_hugging_face_dataset_qa_pairs(
# #   "combined",
# #   hf_dataset_id="anthonymeo/combined-chatML", # The HF dataset id (eg, org/dataset) that contains ChatML format in a 'messages' column.
# #   dataset_split="train", # The name of the dataset split to use, eg, "train", "train_sft", etc..
# #   data_format="chatml" # The format of the data in the dataset. Only "chatml" is currently supported, and it can only be single turn, not multi-turn.
# # )
# # # import csv
# # # import json

# # # def convert_csv_to_chatml_json(input_csv, output_json):
# # #     chatml_data = []

# # #     with open(input_csv, mode='r', encoding='utf-8') as infile:
# # #         reader = csv.DictReader(infile)
        
# # #         for row in reader:
# # #             question = row["Question"]
# # #             answer = row["Answer"]

# # #             # Format the question-answer in ChatML
# # #             chatml_conversation = f"<|im_start|>user\n{question}\n<|im_end|>\n<|im_start|>assistant\n{answer}\n<|im_end|>"

# # #             # Append the ChatML conversation as a JSON object
# # #             chatml_data.append({"messages": chatml_conversation})

# # #     # Write the entire list of ChatML conversations to a JSON file
# # #     with open(output_json, mode='w', encoding='utf-8') as outfile:
# # #         json.dump(chatml_data, outfile, indent=4)

# # # # Example usage:
# # # # Example usage:
import csv
import requests
import json

# Define the Ollama API endpoint
OLLAMA_API_URL = "http://localhost:11434/api/generate"

# Function to query Ollama
def query_ollama(question, answer):
    prompt = f"You are generating a markdown formatted, long form dataset that will be used to train LLMs. You are provided with Context, Question and an Answer. Your task is to create a variation of the given answer that has has the same final answer but uses different logic, verbage and formatting. Please give a very detailed and comprehensive response, assuming that the user is not familiar with the topic being discussed. **IMPORTANT** All answers must use the markdown syntax and specifically, must have the sources in a clean markdown format. All math equations shall be surrounded by \"$$\". Please format your final answer so that it can be easily distinguished from the rest of the text.:\n\nQuestion: {question}\nAnswer: {answer}\nExpanded Answer:"
    
    payload = {
        "model": "NEC_Q4",  # Replace with your model name if necessary
        "prompt": prompt,
        "max_length": 8192,  # Adjust as needed
        "stream": True  # Enable streaming
    }

    try:
        # Stream the response from Ollama
        response = requests.post("http://localhost:11434/api/generate", json=payload, stream=True)
        response.raise_for_status()  # Raises HTTPError if the response is an error
        
        expanded_answer = ""

        # Process the stream of responses chunk by chunk
        for line in response.iter_lines():
            if line:
                # Each line should be a valid JSON object, so parse it
                try:
                    chunk = json.loads(line.decode('utf-8'))
                    expanded_answer += chunk.get('response', '')  # Append each part of the response
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON: {e}")
                    continue

        # Replace actual newlines with the literal "\n" for CSV compatibility
        expanded_answer = expanded_answer.replace("\n", "\\n")
        print(expanded_answer)
        return expanded_answer if expanded_answer else None

    except requests.exceptions.RequestException as e:
        # Handle other request exceptions (e.g., network errors, timeouts)
        print(f"Error querying Ollama: {e}")
        return None

# Function to process the dataset and write each result to CSV
def process_dataset(input_csv, output_csv):
    with open(input_csv, 'r') as infile:
        reader = csv.DictReader(infile)
        fieldnames = ['Question', 'Answer']

        # Write header to output CSV before starting the process
        with open(output_csv, 'w', newline='') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
            writer.writeheader()

        # Process each row and write to CSV immediately after receiving a response
        for row in reader:
            question = row['Question']
            original_answer = row['Answer']
            
            # Send the question and original answer to Ollama
            # Send the question and original answer to Ollama
            expanded_answer = query_ollama(question, original_answer)

            if expanded_answer:
                # Ensure that both question and answer are single-line entries in the CSV
                question = question.replace("\n", "\\n")
                
                # Append the result to the output CSV
                with open(output_csv, 'a', newline='') as outfile:
                    writer = csv.DictWriter(outfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
                    writer.writerow({
                        'Question': question,
                        'Answer': expanded_answer
                    })

# Input and output file paths
input_csv = "/home/ant/Documents/nvme/flask-langchain/conduit_question_answer_pairs3.csv"  # Replace with your input file path
output_csv = "/home/ant/Documents/nvme/flask-langchain/conduit_question_answer_pairs3_expanded_answers.csv"  # Replace with your output file path

process_dataset(input_csv, output_csv)


import json
import re

def extract_question_and_input(content):
    """
    Extracts the question and input from the user's message content.
    """
    sections = {}
    pattern = r'\*\*(.*?)\*\*:(.*?)(?=\n\*\*|$)'
    matches = re.findall(pattern, content, re.DOTALL)
    for key, value in matches:
        sections[key.strip().lower()] = value.strip()
    question = sections.get('question', '')
    input_text = sections.get('input', '')
    return question, input_text

# Read data from open-ai-batchinput.jsonl
input_data = {}
with open('/home/ant/Documents/nvme/flask-langchain/open-ai-batchinput.json', 'r', encoding='utf-8') as infile:
    for line in infile:
        obj = json.loads(line)
        custom_id = obj.get('custom_id')
        body = obj.get('body', {})
        messages = body.get('messages', [])
        # Find the last message from 'user'
        user_messages = [msg for msg in messages if msg.get('role') == 'user']
        if user_messages:
            user_message = user_messages[-1]
            content = user_message.get('content', '')
            # Extract question and input
            question, input_text = extract_question_and_input(content)
            input_data[custom_id] = {'instruction': question, 'input': input_text}
        else:
            input_data[custom_id] = {'instruction': '', 'input': ''}

# Read data from getAnswers.jsonl
answers = {}
with open('/home/ant/Documents/nvme/flask-langchain/getAnswers.jsonl', 'r', encoding='utf-8') as infile:
    for line in infile:
        obj = json.loads(line)
        custom_id = obj.get('custom_id')
        response = obj.get('response', {})
        body = response.get('body', {})
        choices = body.get('choices', [])
        if choices:
            assistant_message = choices[0].get('message', {})
            answer_content = assistant_message.get('content', '')
            answers[custom_id] = answer_content
        else:
            answers[custom_id] = ''

# Combine data into a new dataset
combined_data = []
for custom_id, data in input_data.items():
    instruction = data.get('instruction', '')
    input_text = data.get('input', '')
    answer = answers.get(custom_id, '')
    combined_data.append({
        'instruction': instruction,
        'input': input_text,
        'answer': answer
    })

# Save the combined data to a new JSON file
with open('openAI_dataset.json', 'w', encoding='utf-8') as outfile:
    json.dump(combined_data, outfile, indent=2)
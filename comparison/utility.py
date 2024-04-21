import csv
import datetime
from openai import OpenAI
import json
import os

import utility

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            file_contents = file.read()
            return file_contents
    except FileNotFoundError:
        print("File not found.")
        return None
    except Exception as e:
        print("An error occurred:", e)
        return None

API_KEY = {
    "nick": "sk-proj-t2U9wT3sqbfXNunqLXLbT3BlbkFJsOB54HEqfEaluM0u1utd"
}

API_KEY_USE = 'nick'

DEFAULT_TOKEN_LIMIT = 200

RUNTIMESTAMP = datetime.datetime.now().strftime("%Y.%m.%d_%H.%M.%S")

client = OpenAI(api_key=API_KEY[API_KEY_USE])

def read_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON in file '{file_path}'.")
        return None

def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        try:
            os.makedirs(folder_path)
            print(f"Folder '{folder_path}' created successfully.")
        except Exception as e:
            print(f"Error occurred while creating folder: {e}")
    # else:
        # print(f"Folder '{folder_path}' already exists.")

def response_object_to_json_type_object(response):
    parsed = {
        "id": response.id,
        "object": response.object,
        "created": response.created,
        "model": response.model,
        "usage": {
            "prompt_tokens": response.usage.prompt_tokens,
            "completion_tokens": response.usage.completion_tokens,
            "total_tokens": response.usage.total_tokens
        },
        "choices": []
    }
    for choice in response.choices:
        parsed["choices"].append(
            {
                "message": {
                    "role": choice.message.role,
                    "content": choice.message.content
                },
                "finish_reason": choice.finish_reason,
                "index": choice.index
            }
        )
    return parsed

def save_response_to_file(response, foldername = 'saved_responses'):
    create_folder_if_not_exists(foldername)
    parsed = response_object_to_json_type_object(response)
    save_variable_to_file(parsed, f"{foldername}/{response.id}.log")

def save_to_previous_messages(message, foldername = 'message_history', filename=RUNTIMESTAMP):
    create_folder_if_not_exists(foldername)
    save_variable_to_file(message, f'{foldername}/{filename}.log')

def last_line_ends_with_brace(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            while lines and not lines[-1].strip():
                lines.pop()
            if lines and lines[-1].rstrip().endswith('}'):
                return True
            else:
                return False
    except FileNotFoundError:
        #print("File not found for brace detection.")
        return False
    except Exception as e:
        print("An error occurred:", e)
        return False

def save_variable_to_file(variable, filename = 'saved_variables.log'):
    notfirst = last_line_ends_with_brace(filename)
    try:
        with open(filename, 'a') as file:
            if notfirst: file.write(',\n')
            json.dump(variable, file, indent=4)
        # print("Variable saved to file successfully.")
    except Exception as e:
        print(f"Error occurred while saving variable to file: {e}")

def chat(prompt, messages=[], token_limit = DEFAULT_TOKEN_LIMIT):
    messages.append({'role': 'user', 'content': prompt})
    save_to_previous_messages({'role': 'user', 'content': prompt})
    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=messages,
        max_tokens=token_limit
    )
    save_response_to_file(response)
    save_to_previous_messages({'role': response.choices[0].message.role, 'content': response.choices[0].message.content})
    return response.choices[0]

def get_column_data(filename, delimiter=",", column=0):
  data = []
  try:
    with open(filename, 'r') as file:
      reader = csv.reader(file, delimiter=delimiter)
      # Skip header row if it exists
      next(reader, None)  
      for row in reader:
        # Assuming column A is at index 0 (change if needed)
        data.append(row[column])
  except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
  return data

def get_restaurant_data(filename='restaurants.json'):
    return read_json_file(file_path=filename)
    
def get_queries(filename='queries.csv'):
    return get_column_data(filename)
    

            

    









# file_helper.py
import json
import os

# The file where we store our data
Data_file = "my_expenses.json"

def save_to_file(expense_list):
    # Convert list of objects to list of dictionaries
    data_to_save = [item.to_dictionary() for item in expense_list]
    
    try:
        with open(Data_file, 'w') as f:
            json.dump(data_to_save, f)
        print(">> Saved successfully!")
    except Exception as e:
        print(f"Error saving file: {e}")

def load_from_file():
    # Check if file exists first
    if not os.path.exists(Data_file):
        return [] # Return empty list if no file found
    
    try:
        with open(Data_file, 'r') as f:
            return json.load(f)
    except:
        print("Could not read file, starting fresh.")
        return []
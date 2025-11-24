# logic.py
from expense import Expense
import file_helper
import inputs

# Load data as soon as we import this module
data_from_file = file_helper.load_from_file()
my_expenses = []

# Convert the raw dictionaries back into Expense objects
for item in data_from_file:
    # Handling cases where data might come from dict or object logic
    amount = item.get('amount')
    category = item.get('category')
    desc = item.get('description')
    
    # Re-create the object
    obj = Expense(amount, category, desc)
    # If the saved date exists, use it, otherwise it defaults to today
    if 'date' in item:
        obj.date = item['date']
        
    my_expenses.append(obj)

def add_new_expense():
    print("\n--- Add a New Entry ---")
    amount = inputs.ask_for_number("How much did you spend? : ")
    category = inputs.ask_for_text("Category (Food, Travel, etc): ")
    desc = inputs.ask_for_text("Short Description: ")
    
    new_item = Expense(amount, category, desc)
    my_expenses.append(new_item)
    
    # Save immediately so we don't lose data
    file_helper.save_to_file(my_expenses)

def show_all():
    print("\n--- Your Expense History ---")
    if len(my_expenses) == 0:
        print("Nothing to show yet!")
        return

    print(f"{'ID':<5} | {'Date':<12} | {'Category':<15} | {'Amount':<10} | {'Note'}")
    print("-" * 65)
    
    for i, exp in enumerate(my_expenses):
        # print each row clearly
        print(f"{i+1:<5} | {exp.date:<12} | {exp.category:<15} | ₹{exp.amount:<9} | {exp.description}")
    print("-" * 65)

def show_total():
    print("\n--- Summary ---")
    total_money = 0
    for x in my_expenses:
        total_money += x.amount
    
    print(f"You have spent a total of: ₹{total_money}")

def delete_entry():
    show_all()
    if len(my_expenses) == 0:
        return
        
    print("\nWhich one do you want to delete?")
    choice = inputs.ask_for_number("Enter the ID number: ")
    index = int(choice) - 1
    
    if index >= 0 and index < len(my_expenses):
        removed = my_expenses.pop(index)
        file_helper.save_to_file(my_expenses)
        print(f"Removed entry: {removed.description}")
    else:
        print("Invalid ID number.")
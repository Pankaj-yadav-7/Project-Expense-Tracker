import logic

def main_menu():
    print("================================")
    print("       EXPENSE   TRACKER        ")
    print("================================")
    print("1. Add Expense")
    print("2. View History")
    print("3. Check Total Spending")
    print("4. Delete an Entry")
    print("5. Exit")

def run():
    while True:
        main_menu()
        choice=input("Select an option (1-5): ")
        if choice =="1":
            logic.add_new_expense()
        elif choice =="2":
            logic.show_all()
        elif choice =="3":
            logic.show_total()
        elif choice =="4":
            logic.delete_entry()
        elif choice =="5":
            print("Saving data...Closing program........")
            break
        else:
            print("Invalid input")

if __name__ == "__main__":
    run()
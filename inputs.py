def ask_for_number(message):
    # Keeps asking until the user gives a valid number
    while True:
        user_text = input(message)
        try:
            value = float(user_text)
            if value < 0:
                print("Please enter a positive amount.")
            else:
                return value
        except ValueError:
            print("Oops! That doesn't look like a number. Try again.")

def ask_for_text(message):
    # Ensures the user doesn't just press 'Enter' without typing
    while True:
        text = input(message).strip()
        if len(text) > 0:
            return text
        else:
            print("This field cannot be empty.")

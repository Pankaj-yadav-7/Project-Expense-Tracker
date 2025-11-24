import datetime

# This class represents a single expense entry
class Expense:
    def __init__(self, amount, category, description):
        self.amount = amount
        self.category = category
        self.description = description
        # setting the date automatically to today's date
        self.date = datetime.date.today().strftime("%Y-%m-%d")

    def to_dictionary(self):
        #save data to the JSON file easily
        return {"amount": self.amount,"category": self.category,"description": self.description,"date": self.date}

    def __str__(self):
        # This helps print the object nicely for debugging
        return f"{self.date} | {self.category}: ₹{self.amount}"
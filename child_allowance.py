from datetime import datetime
import csv

class Child:

    num_of_children = 0


    def __init__(self, childname, description, transaction_amount=2):
        self.description = description
        self.transaction_amount = transaction_amount
        # self.num_of_transactions = 0

    def add_money(self):
        """"Add amount for period."""
        self.current_amount = self.current_amount + self.raise_amount
        self.num_of_transactions += 1
        self.num_of_add += 1


    def use_money(self, used_amount):
        """Subtracts from current_amount when child uses money."""
        self.current_amount + (self.transaction_amount)  # addition used; cus x + (-y) is correct
        self.num_of_transactions += 1
        self.num_of_use += 1


    def get_current_data(self):
        """Reads latest entry (last line) in database for instance."""
        with open('sample_csv_michael.csv', 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=';')
            return list(reader)[-1]


    def store_transaction(self, data):
        """Stores transaction in database."""
        childname = data[0]
        current_amount = int(data[4])
        transaction_id = int(data[1]) + 1
        transaction_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_amount = current_amount + self.transaction_amount

        print(f"{childname}  {transaction_id}  {transaction_date}  {self.transaction_amount}  {new_amount}  {self.description}")

        with open('sample_csv_michael.csv', mode='a') as child_file:
            child_writer = csv.writer(child_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            child_writer.writerow([
                childname,  # childname
                transaction_id,  # transaction_id
                transaction_date,  # transaction_date
                self.transaction_amount,  # transaction_amount
                new_amount,  # current_amount
                self.description  # description
            ])


if __name__ == '__main__':
    # Child(name, description, amount)
    michael = Child('Michael', 'w51', 2)
    current_data = michael.get_current_data()
    michael.store_transaction(current_data)

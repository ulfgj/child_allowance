from datetime import datetime
import csv

class Child:

    num_of_children = 0


    def __init__(self, childname, description, transaction_amount=2):
        self.childname = childname
        self.description = description
        self.transaction_amount = transaction_amount


    def get_current_data(self):
        """Reads latest entry (last line) in database for instance."""
        with open('sample_csv_michael.csv', 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=';')
            return list(reader)[-1]


    def store_transaction(self, data):
        """Stores transaction in database."""
        current_amount = int(data[4])
        transaction_id = int(data[1]) + 1
        transaction_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_amount = current_amount + self.transaction_amount

        print(f"{self.childname}  {transaction_id}  {transaction_date}  {self.transaction_amount}  {new_amount}  {self.description}")

        with open('sample_csv_michael.csv', mode='a') as child_file:
            child_writer = csv.writer(child_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            child_writer.writerow([
                self.childname,  # childname
                transaction_id,  # transaction_id
                transaction_date,  # transaction_date
                self.transaction_amount,  # transaction_amount
                new_amount,  # current_amount
                self.description  # description
            ])


if __name__ == '__main__':
    # Child(name, description, amount)
    michael = Child('Michael', 'candy', -5)
    current_data = michael.get_current_data()
    michael.store_transaction(current_data)

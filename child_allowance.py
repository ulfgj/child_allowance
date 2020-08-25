from datetime import datetime
import csv

class Child:


    def __init__(self, childname, description, transaction_amount=2):
        self.childname = childname
        self.description = description
        self.transaction_amount = transaction_amount


    def get_current_data(self):
        """Reads latest entry (last line) in database for instance."""
        with open(f'{self.childname}_sample.csv', 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=';')
            return list(reader)[-1]


    def store_transaction(self, data):
        """Stores transaction in database."""
        current_amount = int(data[4])
        transaction_id = int(data[1]) + 1
        transaction_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_amount = current_amount + self.transaction_amount

        print(f"{self.childname}  {transaction_id}  {transaction_date}  {self.transaction_amount}  {new_amount}  {self.description}")

        with open(f'{self.childname}_sample.csv', mode='a') as child_file:
            child_writer = csv.writer(child_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            child_writer.writerow([
                self.childname,
                transaction_id,
                transaction_date,
                self.transaction_amount,
                new_amount,
                self.description
            ])


if __name__ == '__main__':
    # Child(name, description, amount)
    child1 = Child('child1', 'candy', -5)
    current_data = child1.get_current_data()
    child1.store_transaction(current_data)

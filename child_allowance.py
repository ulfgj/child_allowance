from datetime import datetime
import csv
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('--create', action='store_true')
ap.add_argument('childname')
ap.add_argument('amount', type=int)
ap.add_argument('description', nargs='?')
args = ap.parse_args()

transaction_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
header = ['childname', 'transaction_id', 'transaction_date', 'transaction_amount', 'current_amount', 'description']


class Child:

    def __init__(self, childname, description, transaction_amount=2):
        self.childname = childname
        self.description = description
        self.transaction_amount = transaction_amount


    def get_current_data(self):
        """Reads latest entry (last line) in database for instance."""
        with open(f'{self.childname}_log.csv', 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=';')
            return list(reader)[-1]


    def create_child(self):
        """Setup a file for a new child to track."""
        child_data = [
            self.childname,
            1,  # transaction id
            transaction_date,
            self.transaction_amount,
            self.transaction_amount,  # no old amount existed before
            'creation of record'
        ]
        with open(f'{self.childname}_log.csv', mode='w+') as child_file:
            child_writer = csv.writer(child_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            child_writer.writerow(header)
            child_writer.writerow(child_data)


    def store_transaction(self, data):
        """Stores transaction in database."""
        current_amount = int(data[4])
        transaction_id = int(data[1]) + 1
        transaction_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_amount = current_amount + self.transaction_amount
        # print(f"{self.childname}  {transaction_id}  {transaction_date}  {self.transaction_amount}  {new_amount}  {self.description}")
        child_data = [
            self.childname,
            transaction_id,
            transaction_date,
            self.transaction_amount,
            new_amount,
            self.description
        ]
        with open(f'{self.childname}_log.csv', mode='a+') as child_file:
            child_writer = csv.writer(child_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            child_writer.writerow(child_data)


if __name__ == '__main__':

    child = Child(args.childname, args.description, args.amount)
    if args.create:
        child.create_child()
    else:
        print(f"current: {child.get_current_data()}")
        current_data = child.get_current_data()
        child.store_transaction(current_data)
        print(f"updated: {child.get_current_data()}")

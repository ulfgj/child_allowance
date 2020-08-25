

class Child:

    num_of_children = 0


    def __init__(self, name, period, raise_amt=2, used_amt=0):
        self.raise_amt = raise_amt
        self.used_amt
        self.num_of_transactions = 0
        self.num_of_add = 0
        self.num_of_use = 0


    def add_money(self):
        """"Add amount for period."""
        self.current_amt = self.current_amt + self.raise_amt
        self.num_of_transactions += 1
        self.num_of_add += 1

    def use_money(self, used_amt):
        """Subtracts from current_amt when child uses money."""
        self.current_amt - self.used_amt
        self.num_of_transactions += 1
        self.num_of_use += 1


    def get_current_data(self):
        """Reads latest entry in  database for instance."""
        pass


    def store_transaction(self):
        """Stores transaction in database."""

        pass


misa = Child('michael ulf rexa', 'w28', )

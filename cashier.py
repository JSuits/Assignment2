class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("Please Insert Funds.")
        dollars = input("How many dollars?")
        quarters = input("How many quarters?")
        dimes = input("How many dimes?")
        nickels = input("How many nickels?")
        self.amount = float(dollars) + .25 * float(quarters) + .1 * float(dimes) + .05 * float(nickels)

    def transaction_result(self, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        self.cost = cost
        change = float(self.amount) - float(self.cost)
        if (float(self.amount) < float(self.cost)):
            return False;
        else:
            if (float(self.amount) > float(self.cost)):
                print('Here is $', change, 'in change')
            else:
                print('No change')
            return True
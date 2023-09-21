import data
import cashier

class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        if (data.resources['bread'] >= data.recipes[ingredients]['ingredients']['bread']
                and data.resources['ham'] >= data.recipes[ingredients]['ingredients']['ham']
                and data.resources['cheese'] >= data.recipes[ingredients]['ingredients']['cheese']):
            return True
        else:
            return False

    def make_sandwich(self, sandwich_size, order_ingredients):
        self.order_ingredients = order_ingredients
        self.sandwich_size = sandwich_size
        self.machine_resources['bread'] -= self.order_ingredients['bread']
        self.machine_resources['ham'] -= self.order_ingredients['ham']
        self.machine_resources['cheese'] -= self.order_ingredients['cheese']
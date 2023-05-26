class CoffeeMaker:
    """Models the machine that makes the coffee."""
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        """Prints a report of all resources."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resources_sufficient(self, drink):
        """Returns True when order can be made, False if ingeredients are insufficient."""
        can_make = True
        for item in drink.ingeredients:
            if drink.ingeredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make
    
    def make_coffee(self, order):
        """Deducts the required ingredients from the resources."""
        for item in order.ingeredients:
            self.resources[item] -= order.ingeredients[item]
        print(f"here is your {order.name} ☕️.Enjoy!")

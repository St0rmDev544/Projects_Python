class MenuItem:
    """Code below models each Menu Item"""
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingeredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }

class Menu:
    """"Code below models the menu with drinks"""
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    def get_items(self):
        """Code Below returns ALL the names of AVAILABLE menu items"""
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options
    
    def find_drink(self, order_name):
        """Code below searches the menu for a particular drink by its name, returns that item if it exists, otherwise returns none"""
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Unfortunately Venta seems to have fallen asleep and that item is no longer available...")

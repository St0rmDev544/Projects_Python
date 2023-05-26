class MoneyMachine:

    CURRENCY = "blobby Snack"

    COIN_VALUES = {
        "yummy treat": 0.25,
        "meh treat": 0.10,
        "cheap treat": 0.05,
        "crumbs": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """prints current profit"""
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """Returns the total calculated from treats inserted"""
        print("Please Insert treats.")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
        return self.money_received
    
    def make_payment(self, cost):
        """"Returns True when payment is accepted, or False if insufficient."""
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in treats.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry that is not enough treats, you can do better. Treats returned.")
            self.money_received = 0
            return False

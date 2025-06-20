from housing import Housing
from person import Buyer


class Sale:
    def __init__(self, housing: Housing, price: float):
        self.housing = housing
        self.price = price

    def sell(self, buyer: Buyer):
        self.housing.change_owner(buyer)
        print(f"Sold to ${buyer.name}")
        self.housing.print_info()


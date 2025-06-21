from housing import Housing
from person import Renter


# An abstract class
class Rent:
    def __init__(self, housing: Housing, price: float):
        self.renter = Renter
        self.housing = housing
        self.price = price

    # Counts overall price of rent
    def overall_price(self):
        raise Exception("Unimplemented")

    # Changes renter
    def renting(self, renter: Renter):
        self.renter = renter
        self.housing.print_info()


class RentForDay(Rent):
    def __init__(self, housing: Housing, price: float, days_count: int):
        Rent.__init__(self, housing, price)
        self.days_count = days_count

    def overall_price(self):
        return self.price * self.days_count


class RentForMonth(Rent):
    def __init__(self, housing: Housing, price: float, months_count: int):
        Rent.__init__(self, housing, price)
        self.months_count = months_count

    def overall_price(self):
        return self.price * self.months_count


class RentForYear(Rent):
    def __init__(self, housing: Housing, price: float, years_count: int):
        Rent.__init__(self, housing, price)
        self.years_count = years_count

    def overall_price(self):
        return self.price * self.years_count

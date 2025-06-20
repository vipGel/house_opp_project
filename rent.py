from housing import Housing


class Rent:
    def __init__(self, housing: Housing, price: float):
        self.housing = housing
        self.price = price


class RentForDay(Rent):
    def __init__(self, housing: Housing, price: float, days_count: int):
        Rent.__init__(self, housing, price)
        self.days_count = days_count


class RentForMonth(Rent):
    def __init__(self, housing: Housing, price: float, months_count: int):
        Rent.__init__(self, housing, price)
        self.months_count = months_count


class RentForYear(Rent):
    def __init__(self, housing: Housing, price: float, years_count: int):
        Rent.__init__(self, housing, price)
        self.years_count = years_count

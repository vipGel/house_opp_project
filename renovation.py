# An abstract class
class Renovation:
    def __init__(self, name):
        self.name = name


class EuroRenovation(Renovation):
    pass


class BasicRenovation(Renovation):
    pass


class NoRenovation(Renovation):
    pass

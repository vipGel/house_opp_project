class Person:
    def __init__(self, name: str):
        self.name = name

    def print_info(self):
        raise Exception("Unimplemented")


class Owner(Person):
    def __init__(self, name: str):
        Person.__init__(self, name)


class Buyer(Person):
    def __init__(self, name: str):
        Person.__init__(self, name)
        # self.bought: list[Housing] = []
    #
    # def print_info(self):
    #     print(f"${self.name} has:")
    #     if len(self.bought) == 0:
    #         print("No houses  :(")
    #         return
    #     for i in self.bought:
    #         i.print_info()


class Renter(Person):
    def __init__(self, name: str):
        Person.__init__(self, name)
        # self.rents: list[Housing] = []

    # def renting(self, housing: Housing):
    #     self.rents.append(housing)
    #
    # def print_info(self):
    #     print(f"${self.name} rents:")
    #     if len(self.rents) == 0:
    #         print("No houses  :(")
    #         return
    #     for i in self.rents:
    #         i.print_info()

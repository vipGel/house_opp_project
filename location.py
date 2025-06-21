class Location:
    def info(self) -> str:
        raise Exception("Unimplemented!")


class Downtown(Location):
    def __init__(self, city_name):
        self.city_name = city_name

    def info(self):
        return f"Downtown of {self.city_name}"


class Outskirts(Location):
    def __init__(self, city_name):
        self.city_name = city_name

    def info(self):
        return f"Outskirts of {self.city_name}"


class Village(Location):
    def __init__(self, village_name):
        self.city_name = village_name

    def info(self):
        return f"Village named {self.city_name}"


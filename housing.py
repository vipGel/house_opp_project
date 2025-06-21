from location import Location
from person import Person

from renovation import Renovation


class Housing:
    def __init__(self, area: float, location: Location, owner: Person, room_count: int):
        self.area = area
        self.location = location
        self.owner = owner
        self.room_count = room_count

    def print_info(self):
        print(f"Area: {self.area}")
        print(f"Location: {self.location.info()}")
        print(f"Owner: ${self.owner.name}")
        print(f"Roon count: {self.room_count}")

    def change_owner(self, new_owner: Person):
        self.owner = new_owner


class Apartment(Housing):
    def __init__(self, area: float, location: Location, owner: Person, room_count: int, floor: int,
                 renovation: Renovation):
        Housing.__init__(self, area, location, owner, room_count)
        self.floor = floor
        self.renovation = renovation

    def print_info(self):
        Housing.print_info(self)
        print(f"Floor: {self.floor}")
        print(f"Renovation: {self.renovation.name}")


class House(Housing):
    def __init__(self, area: float, location: Location, owner: Person, room_count: int,
                 overall_area: float,
                 renovation: Renovation, floor_count: int):
        Housing.__init__(self, area, location, owner, room_count)
        self.overall_area = overall_area
        self.renovation = renovation
        self.floor_count = floor_count

    def print_info(self):
        Housing.print_info(self)
        print(f"Overall area: {self.overall_area}")
        print(f"Floor count: {self.floor_count}")
        print(f"Renovation: {self.renovation.name}")


class Penthouse(Apartment):
    def __init__(self, area: float, location: Location, owner: Person, room_count: int, floor: int,
                 renovation: Renovation, floor_count: int):
        Housing.__init__(self, area, location, owner, room_count)
        self.floor = floor
        self.renovation = renovation
        self.floor_count = floor_count

    def print_info(self):
        Housing.print_info(self)
        print(f"Floor: {self.floor}")
        print(f"Floor count: {self.floor_count}")
        print(f"Renovation: {self.renovation.name}")

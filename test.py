from housing import House
from location import Downtown
from person import Owner, Buyer
from renovation import EuroRenovation
from rent import RentForDay, RentForMonth, RentForYear
from sale import Sale

euro_renovation = EuroRenovation("EuroRenovation")
warsaw_downtown = Downtown("Warsaw")
owner = Owner("John Owner")
buyer = Buyer("John Buyer")

def test_change_owner():

    house = House(100, warsaw_downtown, owner, 4, 150, euro_renovation, 2)

    assert house.owner == owner
    house.change_owner(buyer)
    assert house.owner == buyer

def test_rent_overall_price_for_days():
    house = House(100, warsaw_downtown, owner, 4, 150, euro_renovation, 2)
    rent = RentForDay(house, 1000, 7)

    assert rent.overall_price() == 7000

def test_rent_overall_price_for_months():
    house = House(100, warsaw_downtown, owner, 4, 150, euro_renovation, 2)
    rent = RentForMonth(house, 3000, 6)

    assert rent.overall_price() == 18000
def test_rent_overall_price_for_years():
    house = House(100, warsaw_downtown, owner, 4, 150, euro_renovation, 2)
    rent = RentForYear(house, 10000, 2)

    assert rent.overall_price() == 20000

def test_sale():
    house = House(100, warsaw_downtown, owner, 4, 150, euro_renovation, 2)
    sale = Sale(house, 100000)
    assert sale.housing.owner == owner
    sale.sell(buyer)
    assert sale.housing.owner == buyer

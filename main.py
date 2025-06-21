from housing import Apartment, House
from location import Downtown, Outskirts
from person import Buyer, Renter, Owner
from renovation import EuroRenovation, BasicRenovation
from rent import Rent, RentForMonth
from sale import Sale


def main():
    euro_renovation = EuroRenovation("EuroRenovation")
    basic_renovation = BasicRenovation("EuroRenovation")

    warsaw_downtown = Downtown("Warsaw")
    warsaw_outskirts = Outskirts("Warsaw")

    owner = Owner("John Owner")
    print("Yeah, I own houses")

    apartment = Apartment(70, warsaw_downtown, owner, 4, 5, euro_renovation)
    house = House(100, warsaw_outskirts, owner, 4, 150, basic_renovation, 2)
    apartment.print_info()
    house.print_info()
    house_sale = Sale(house, 1000000)
    apartment_rent = RentForMonth(apartment, 3000, 6)

    buyer = Buyer("John Buyer")
    print("I'm gonna buy a house")
    house_sale.sell(buyer)
    # owner.sell(house)
    # buyer.buy(house)
    print("I bought a house")

    renter = Renter("John Renter")
    print("I'm gonna rent an apartment")
    # renter.print_info()
    # renter.renting(apartment)
    print("I'm renting")
    apartment_rent.renting(renter)

if __name__ == '__main__':
    main()

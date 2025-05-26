class L1BartenderDrinks(object):
    """https://www.codewars.com/kata/568dc014440f03b13900001d/train/python"""
    def __init__(self):
        pass

    @staticmethod
    def get_drink_by_profession(param: str) -> str:
        drinks_by_prof = {
            "jabroni": "Patron Tequila",
            "school counselor": "Anything with Alcohol",
            "programmer": "Hipster Craft Beer",
            "bike gang member": "Moonshine",
            "politician": "Your tax dollars",
            "rapper": "Cristal"
        }
        return drinks_by_prof.get(param.lower(), "Beer")

    def demo(self):
        print(f"{self.get_drink_by_profession('Programmer')=}")
        print(f"{self.get_drink_by_profession('programmer')=}")
        print(f"{self.get_drink_by_profession('Stranger')=}")

    def test(self):
        from unittest import TestCase
        TestCase().assertEqual(self.get_drink_by_profession("jabrOni"), "Patron Tequila", "'Jabroni' should map to 'Patron Tequila'")
        TestCase().assertEqual(self.get_drink_by_profession("scHOOl counselor"), "Anything with Alcohol", "'School Counselor' should map to 'Anything with alcohol'")
        TestCase().assertEqual(self.get_drink_by_profession("prOgramMer"), "Hipster Craft Beer", "'Programmer' should map to 'Hipster Craft Beer'")
        TestCase().assertEqual(self.get_drink_by_profession("bike ganG member"), "Moonshine", "'Bike Gang Member' should map to 'Moonshine'")
        TestCase().assertEqual(self.get_drink_by_profession("poLiTiCian"), "Your tax dollars", "'Politician' should map to 'Your tax dollars'")
        TestCase().assertEqual(self.get_drink_by_profession("rapper"), "Cristal", "'Rapper' should map to 'Cristal'")
        TestCase().assertEqual(self.get_drink_by_profession("pundit"), "Beer", "'Pundit' should map to 'Beer'")
        TestCase().assertEqual(self.get_drink_by_profession("Pug"), "Beer", "'Pug' should map to 'Beer'")


def main():
    print("L1: Bartender, drinks!")
    L1BartenderDrinks().demo()
    L1BartenderDrinks().test()


if __name__ == "__main__":
    main()

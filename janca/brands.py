class Address(object):
    @staticmethod
    def get_brno():
        return "Brno"

    @staticmethod
    def get_vienna():
        return "Vienna"

    @staticmethod
    def get_praha():
        return "Praha"


class Project(object):
    @staticmethod
    def get_spoluvlastnici():
        return "Spoluvlastnici"

    @staticmethod
    def get_mediation():
        return "Mediation"


class Brands(object):
    def __init__(self):
        self._brands = {
            "Artin": {
                "Address": Address().get_brno,
                "Project": Project().get_spoluvlastnici
            },
            "Cetin": {
                "Address": Address().get_praha,
                "Project": Project().get_mediation
            },
            "Drei": {
                "Address": Address().get_vienna,
                "Project": Project().get_mediation
            }
        }

    def get_brands(self):
        return self._brands.keys()

    def get_address(self, brand):
        return self._brands[brand]["Address"]()

    def get_project(self, brand):
        return self._brands[brand]["Project"]()


def main():
    print("Brands")
    for brand in Brands().get_brands():
        print("%s: %s - %s" % (brand, Brands().get_address(brand), Brands().get_project(brand)))


if __name__ == "__main__":
    main()

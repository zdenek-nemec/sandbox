class Heroes3(object):
    def __init__(self):
        super(Heroes3, self).__init__()
        self._army_size = {
            "Few" : (1, 4),
            "Several" : (5, 9),
            "Pack" : (10, 19),
            "Lots" : (20, 49),
            "Horde" : (50, 100),
            "Throng" : (100, 249),
            "Swarm" : (250, 499),
            "Zounds" : (500, 999),
            "Legion" : (1000, float("inf"))
        }

    def get_all(self):
        return self._army_size

    def get_army_description(self, size):
        for key in self._army_size:
            minimum, maximum = self._army_size[key]
            if size >= minimum and size <= maximum:
                return key
        else:
            return "Unknown"


def main():
    print("Hello, Heroes of Might and Magic 3!")


if __name__ == "__main__":
    main()

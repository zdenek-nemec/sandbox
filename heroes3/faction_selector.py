import random


class Faction(object):
    def __init__(self):
        self._faction_list = [
            "Castle",
            "Rampart",
            "Tower",
            "Inferno",
            "Necropolis",
            "Dungeon",
            "Stronghold",
            "Fortress",
            "Conflux"
        ]

    def get_random(self):
        return random.choice(self._faction_list)


def main():
    print("Hello, Heroes of Might and Magic 3 Faction Selector!")
    print(Faction().get_random())


if __name__ == "__main__":
    main()

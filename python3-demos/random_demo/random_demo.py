import random


class RandomDemo(object):
    """RandomDemo"""
    def __init__(self):
        super(RandomDemo, self).__init__()

    def demo_choice(self):
        sequence = [3, 7, 42]
        return random.choice(sequence)

    def demo_randint(self):
        minimum = 0
        maximum = 100
        return random.randint(minimum, maximum)


def main():
    print("random_demo")

    print("random.choice:", RandomDemo().demo_choice())
    print("random.randint:", RandomDemo().demo_randint())


if __name__ == "__main__":
    main()

class Square(object):
    def __init__(self):
        pass

    def get_square(self, side):
        return side ** 2


def main():
    print(Square().get_square(2))


if __name__ == "__main__":
    main()

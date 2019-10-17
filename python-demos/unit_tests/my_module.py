class Square(object):
    """docstring for Square"""
    def __init__(self):
        pass

    def get_area(self, side):
        if side < 0:
            raise ValueError
        return side**2


def main():
    print("Hello, World!")
    print(Square().get_area(2))

    my_object = []
    print(type(my_object))
    if type(my_object) == list:
        print("Yes")
    if isinstance(my_object, list):
        print("Yes")

    my_list = [1, 2, 3, 4, "five", 6, 7.0]
    integers = filter(lambda x: not isinstance(x, int), my_list)
    print(list(integers))
    print(any(not isinstance(x, int) for x in my_list))
    print(any(not isinstance(x, int) for x in my_list[:4]))



if __name__ == "__main__":
    main()

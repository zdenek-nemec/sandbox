class Demos(object):
    def demo_type(self):
        print(type(1))
        print(type(1.0))
        print(type(''))
        print(type(()))
        print(type([]))
        print(type({}))


def main():
    Demos().demo_type()


if __name__ == '__main__':
    main()

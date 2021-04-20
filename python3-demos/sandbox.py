class DemoReturnMultipleValues(object):
    """Demo: Return multiple values"""
    def __init__(self):
        pass

    def run(self):
        a, b = self.increment_xy(1, 2)
        print("Results: ", a, b)

    def increment_xy(self, x, y):
        return x + 1, y + 1


def main():
    DemoReturnMultipleValues().run()


if __name__ == "__main__":
    main()

import argparse


DEFAULT_ARGUMENT_B = "X"


def main():
    print("Hello, World!")
    argument_parser = argparse.ArgumentParser(prog="parse_arguments_demo")
    argument_parser.add_argument("--argument_a", "-a")
    argument_parser.add_argument("--argument_b", "-b", default=DEFAULT_ARGUMENT_B)
    argument_parser.add_argument("--argument_c", "-c", choices=["111", "222", "333"])

    print(argument_parser.parse_args().argument_a)
    print(argument_parser.parse_args().argument_b)
    print(argument_parser.parse_args().argument_c)


if __name__ == "__main__":
    main()

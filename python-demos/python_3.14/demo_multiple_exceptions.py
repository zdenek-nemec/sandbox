"""https://www.root.cz/clanky/python-3-14-t-retezce-barvicky-lepsi-napoveda-a-odchazejici-gil/#k13"""

import sys


"""Pre 3.14"""
def demo_multiple_exceptions_old_style():
    try:
        with open("non_existing_file", "r") as fin:
            pass
        with open("/", "w") as fout:
            pass
    except (FileNotFoundError, PermissionError):  # Requires parentheses
        print("Old-style: Error as expected")


"""Python 3.14+"""
def demo_multiple_exceptions_new_style():
    try:
        with open("non_existing_file", "r") as fin:
            pass
        with open("/", "w") as fout:
            pass
    except FileNotFoundError, PermissionError:  # No parentheses required
        print("New-style: Error as expected")


"""Python 3.14+"""
def demo_multiple_exceptions_new_style_as_e():
    try:
        with open("non_existing_file", "r") as fin:
            pass
        with open("/", "w") as fout:
            pass
    except (FileNotFoundError, PermissionError) as e:  # Parentheses still required when using "as e"
        print(f"New-style: Error as expected, {e}")


def main():
    print("Hello. This is a demo of multiple exceptions")

    print(f"Python: {sys.version}")
    print(f"Environment: {sys.prefix}")

    demo_multiple_exceptions_old_style()
    demo_multiple_exceptions_new_style()
    demo_multiple_exceptions_new_style_as_e()


if __name__ == "__main__":
    main()

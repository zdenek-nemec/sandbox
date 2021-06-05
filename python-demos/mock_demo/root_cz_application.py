"""Implementace logiky aplikace, kterou budeme testovat."""


def function1():
    """Funkce, kterou v testech nahradíme mockem."""
    print("function1 called")
    return "tested function"


def main():
    print("Hello, World!")
    function1()


if __name__ == "__main__":
    main()

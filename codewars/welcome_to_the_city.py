from unittest import TestCase


def say_hello(name: list, city: str, state: str) -> str:
    return f'Hello, {" ".join(name)}! Welcome to {city}, {state}!'


def main():
    print(say_hello(["F", "L"], "C", "S"))
    TestCase().assertEqual(say_hello(['John', 'Smith'], 'Phoenix', 'Arizona'), 'Hello, John Smith! Welcome to Phoenix, Arizona!')
    TestCase().assertEqual(say_hello(['Franklin','Delano','Roosevelt'], 'Chicago', 'Illinois'), 'Hello, Franklin Delano Roosevelt! Welcome to Chicago, Illinois!')
    TestCase().assertEqual(say_hello(['Wallace','Russel','Osbourne'],'Albany','New York'), 'Hello, Wallace Russel Osbourne! Welcome to Albany, New York!')
    TestCase().assertEqual(say_hello(['Lupin','the','Third'],'Los Angeles','California'), 'Hello, Lupin the Third! Welcome to Los Angeles, California!')
    TestCase().assertEqual(say_hello(['Marlo','Stanfield'],'Baltimore','Maryland'), 'Hello, Marlo Stanfield! Welcome to Baltimore, Maryland!')


if __name__ == "__main__":
    main()

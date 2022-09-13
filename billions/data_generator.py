import random

TIME_FORMAT = "%Y-%m-%d %H:%M:%S"
CUSTOMERS = [1, 2, 3, 4]
SITES = ["Alpha", "Beta", "Gamma"]
LOCATIONS = ["N", "E", "S", "W"]


def main():
    print(f"Hello, World!")
    random_customer = random.choice(CUSTOMERS)
    random_site = random.choice(SITES)
    random_location = random.choice(LOCATIONS)
    print(f"{random_customer} {random_site} {random_location}")


if __name__ == "__main__":
    main()

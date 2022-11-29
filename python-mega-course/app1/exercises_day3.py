def exercise1():
    user_input = input("Enter a country: ")
    match user_input.lower():
        case "usa":
            print("Hello")
        case "india":
            print("Namaste")
        case "germany":
            print("Hallo")


def exercise2():
    ingredients = ["john smith", "sen plakay", "dora ngacely"]
    for item in ingredients:
        print(item.title())


def main():
    print("Hello, World!")
    # exercise1()
    exercise2()


if __name__ == "__main__":
    main()

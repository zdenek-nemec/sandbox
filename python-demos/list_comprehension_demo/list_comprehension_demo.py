def main():
    # Standard
    values = []
    for x in range(10):
        if not x % 2:
            values.append(x * x)
    print(values)

    # List comprehension
    values = [x * x for x in range(10) if not x % 2]
    print(values)


if __name__ == "__main__":
    main()

DEFAULT_FILENAME = "input_test_file.txt"


def main():
    filename = DEFAULT_FILENAME
    with open(filename, "r") as text_file:
        for line in text_file:
            print(line[:-1])  # Removing the new-line character


if __name__ == "__main__":
    main()

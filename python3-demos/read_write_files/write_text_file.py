DEFAULT_FILENAME = "output_test_file.txt"
DEFAULT_CONTENT = [
    "Obi-Wan Kenobi: Hello there.",
    "General Grievous: General Kenobi. You are a bold one."
]


def main():
    filename = DEFAULT_FILENAME
    content = DEFAULT_CONTENT;
    with open(filename, "w") as text_file:
        for line in content:
            text_file.write(line + "\n")


if __name__ == "__main__":
    main()

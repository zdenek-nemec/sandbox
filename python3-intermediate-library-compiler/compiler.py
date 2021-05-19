from os import listdir
from os.path import isfile


def main():
    print("Hello, World!")

    directory_content = listdir(".")
    print(directory_content)

    files = [item for item in directory_content if isfile(item)]
    print(files)

    relevant = [item for item in files if item[-4:] == ".scr"]
    print(relevant)


if __name__ == "__main__":
    main()

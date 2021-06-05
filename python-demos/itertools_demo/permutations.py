import itertools


CHARACTERS = "ABCD"


def main():
    characters = CHARACTERS
    for permutation in itertools.permutations(CHARACTERS):
        print(permutation)


if __name__ == "__main__":
    main()

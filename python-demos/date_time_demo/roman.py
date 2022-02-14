def get_decadic_from_list(roman):
    months = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII"]
    return months.index(roman) + 1


def get_roman_from_list(decadic):
    months = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII"]
    return months[decadic - 1]


def get_decadic_from_dict(roman):
    months = {
        "I": 1,
        "II": 2,
        "III": 3,
        "IV": 4,
        "V": 5,
        "VI": 6,
        "VII": 7,
        "VIII": 8,
        "IX": 9,
        "X": 10,
        "XI": 11,
        "XII": 12
    }
    return months[roman]


def get_roman_from_dict(decadic):
    months = {
        1: "I",
        2: "II",
        3: "III",
        4: "IV",
        5: "V",
        6: "VI",
        7: "VII",
        8: "VIII",
        9: "IX",
        10: "X",
        11: "XI",
        12: "XII"
    }
    return months[decadic]


def main():
    for month in ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII"]:
        print(month, get_decadic_from_list(month), get_decadic_from_dict(month))

    for month in range(1, 13):
        print(month, get_roman_from_list(month), get_roman_from_dict(month))


if __name__ == "__main__":
    main()

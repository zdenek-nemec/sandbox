def is_opposite(first: str, second: str) -> bool:
    if {first, second} in [{"NORTH", "SOUTH"}, {"EAST", "WEST"}]:
        return True
    return False


def dir_reduc(arr):
    reduced = []
    for i, item in enumerate(arr):
        if len(reduced) == 0:
            reduced.append(item)
            continue
        if is_opposite(item, reduced[-1]):
            reduced.pop()
        else:
            reduced.append(item)
    return reduced


def main():
    print("ANTB2409's Sandbox")

    # print(is_opposite("NORTH", "SOUTH"))
    # print(is_opposite("SOUTH", "NORTH"))
    # print(is_opposite("EAST", "WEST"))
    # print(is_opposite("WEST", "EAST"))
    # print(is_opposite("WEST", "SOUTH"))

    print(dir_reduc(["NORTH"]), "\n")
    print(dir_reduc(["NORTH", "SOUTH"]), "\n")
    print(dir_reduc(["NORTH", "WEST"]), "\n")

    from unittest import TestCase

    a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
    TestCase().assertEqual(dir_reduc(a), ['WEST'])

    a = ["NORTH", "WEST", "SOUTH", "EAST"]
    TestCase().assertEqual(dir_reduc(a), ["NORTH", "WEST", "SOUTH", "EAST"])
    a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"] # ['WEST']
    TestCase().assertEqual(dir_reduc(a), ['WEST'])
    a = ["NORTH", "SOUTH", "EAST", "WEST", "NORTH", "NORTH", "SOUTH", "NORTH","WEST", "EAST"] # ['NORTH', 'NORTH']
    TestCase().assertEqual(dir_reduc(a), ['NORTH', 'NORTH'])
    a = [] # []
    TestCase().assertEqual(dir_reduc(a), [])
    a=["NORTH","SOUTH","SOUTH","EAST","WEST","NORTH"] # []
    TestCase().assertEqual(dir_reduc(a), [])
    a = ["NORTH","SOUTH","SOUTH","EAST","WEST","NORTH","NORTH"] # ["NORTH"]
    TestCase().assertEqual(dir_reduc(a), ["NORTH"])
    a = ["EAST", "EAST", "WEST", "NORTH", "WEST", "EAST", "EAST", "SOUTH", "NORTH", "WEST"] # ["EAST", "NORTH"]
    TestCase().assertEqual(dir_reduc(a), ["EAST", "NORTH"])
    a = ["NORTH", "EAST", "NORTH", "EAST", "WEST", "WEST", "EAST", "EAST", "WEST", "SOUTH"] # ["NORTH", "EAST"])
    TestCase().assertEqual(dir_reduc(a), ["NORTH", "EAST"])
    a = ["NORTH", "WEST", "SOUTH", "EAST"] # ["NORTH", "WEST", "SOUTH", "EAST"])
    TestCase().assertEqual(dir_reduc(a), ["NORTH", "WEST", "SOUTH", "EAST"])
    a = ['NORTH', 'NORTH', 'EAST', 'SOUTH', 'EAST', 'EAST', 'SOUTH', 'SOUTH', 'SOUTH', 'NORTH']
    TestCase().assertEqual(dir_reduc(a), ['NORTH', 'NORTH', 'EAST', 'SOUTH', 'EAST', 'EAST', 'SOUTH', 'SOUTH'])


if __name__ == "__main__":
    main()

import unittest


def name_shuffler(string: str) -> str:
    return " ".join(string.split()[::-1])


def main():
    """https://www.codewars.com/kata/559ac78160f0be07c200005a/train/python"""
    print("Name Shuffler")

    print(name_shuffler("John Doe"))
    unittest.TestCase().assertEqual(name_shuffler('john McClane'),'McClane john')
    unittest.TestCase().assertEqual(name_shuffler('Mary jeggins'),'jeggins Mary')
    unittest.TestCase().assertEqual(name_shuffler('tom jerry'),'jerry tom')


if __name__ == "__main__":
    main()

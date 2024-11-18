from unittest import TestCase

def remove_url_anchor(url: str) -> str:
    return url.split("#")[0]


def main():
    print(remove_url_anchor("www.codewars.com#about"))
    TestCase().assertEqual(remove_url_anchor("www.codewars.com#about"), "www.codewars.com")
    TestCase().assertEqual(remove_url_anchor("www.codewars.com/katas/?page=1#about"), "www.codewars.com/katas/?page=1")
    TestCase().assertEqual(remove_url_anchor("www.codewars.com/katas/"), "www.codewars.com/katas/")


if __name__ == "__main__":
    main()

from unittest import TestCase


class TitleCase:
    """https://www.codewars.com/kata/5202ef17a402dd033c000009/train/python"""

    @staticmethod
    def title_case(title: str, minor_words: str = "") -> str:
        title_words_lower = title.lower().split(" ")
        minor_words_lower = minor_words.lower().split(" ")
        capitalizator = lambda x: x if x in minor_words_lower else x.capitalize()
        return " ".join([title_words_lower[0].capitalize()] + [capitalizator(word) for word in title_words_lower[1:]])

    def demo(self):
        print(self.title_case("a clash of KINGS", "a an the of"))

    def test(self):
        TestCase().assertEqual(self.title_case(""), "")
        TestCase().assertEqual(self.title_case("a clash of KINGS", "a an the of"), "A Clash of Kings")
        TestCase().assertEqual(self.title_case("THE WIND IN THE WILLOWS", "The In"), "The Wind in the Willows")
        TestCase().assertEqual(self.title_case("the quick brown fox"), "The Quick Brown Fox")


def main():
    print("Title Case")
    title_case = TitleCase()
    title_case.demo()
    title_case.test()


if __name__ == "__main__":
    main()

class CountingDuplicates:
    """Counting Duplicates
    https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/train/python
    """
    @staticmethod
    def duplicate_count(text: str) -> int:
        return len([c for c in set(text.lower()) if text.lower().count(c) > 1])

    def demo(self):
        print(f"{self.duplicate_count('Ahoj')=}")
        print(f"{self.duplicate_count('Hello')=}")

    def test(self):
        from unittest import TestCase
        TestCase().assertEqual(self.duplicate_count(""), 0)
        TestCase().assertEqual(self.duplicate_count("abcde"), 0)
        TestCase().assertEqual(self.duplicate_count("abcdeaa"), 1)
        TestCase().assertEqual(self.duplicate_count("abcdeaB"), 2)
        TestCase().assertEqual(self.duplicate_count("Indivisibilities"), 2)


def main():
    print("Counting Duplicates")

    counting_duplicates = CountingDuplicates()
    counting_duplicates.demo()
    counting_duplicates.test()


if __name__ == "__main__":
    main()

from unittest import TestCase as tc


class StringIncrementer:
    """https://www.codewars.com/kata/54a91a4883a7de5d7800009c/python"""

    @staticmethod
    def increment_string(text:str) -> str:
        f = lambda c: c if "0" <= c <= "9" else ""
        old = "".join([d := "_"] and [d := f(c) for c in text[::-1] if d][::-1])
        new = f"{int(old) + 1 if old else 1 :0{len(old)}}"
        return text[0 : len(text) - len(old)] + new

    def demo(self):
        print(self.increment_string("ahoj123"))
        print(self.increment_string("ahoj123"))
        print(self.increment_string("012ahoj123"))
        print(self.increment_string("ahoj"))
        print(self.increment_string("ahoj01"))
        print(self.increment_string("ahoj9"))
        print(self.increment_string("11"))
        print(self.increment_string("11a"))

    def test(self):
        tc().assertEqual(self.increment_string("foo"), "foo1")
        tc().assertEqual(self.increment_string("foobar001"), "foobar002")
        tc().assertEqual(self.increment_string("foobar1"), "foobar2")
        tc().assertEqual(self.increment_string("foobar00"), "foobar01")
        tc().assertEqual(self.increment_string("foobar99"), "foobar100")
        tc().assertEqual(self.increment_string("foobar099"), "foobar100")
        tc().assertEqual(self.increment_string("fo99obar99"), "fo99obar100")
        tc().assertEqual(self.increment_string(""), "1")


def main():
    print("String incrementer")

    StringIncrementer().demo()
    StringIncrementer().test()


if __name__ == "__main__":
    main()

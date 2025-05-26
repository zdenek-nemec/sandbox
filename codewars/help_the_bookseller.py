class HelpTheBookseller(object):
    """https://www.codewars.com/kata/54dc6f5a224c26032800005c/train/python"""
    def __init__(self):
        pass

    @staticmethod
    def stock_list(stocklist: list, categories: list) -> str:
        if not stocklist:
            return ""

        category_list = {}
        for item in stocklist:
            book, number = item.split(" ")
            if book[0] not in category_list:
                category_list[book[0]] = int(number)
            else:
                category_list[book[0]] += int(number)

        result = ""
        for category in categories:
            result += f"({category} : {category_list[category] if category in category_list else 0}) - "
        return result[:-3]

    def demo(self):
        b = ["ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"]
        c = ["A", "B", "C", "W"]
        print(f"{self.stock_list(b, c)=}")

        b = ["ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60", "DRTYX 60"]
        c = ["A", "B", "C", "W"]
        print(f"{self.stock_list(b, c)=}")

    def test(self):
        from unittest import TestCase

        b = ["ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"]
        c = ["A", "B", "C", "W"]
        TestCase().assertEqual(self.stock_list(b, c), "(A : 20) - (B : 114) - (C : 50) - (W : 0)")

        b = ["BBAR 150", "CDXE 515", "BKWR 250", "BTSQ 890", "DRTY 600"]
        c = ["A", "B", "C", "D"]
        TestCase().assertEqual(self.stock_list(b, c), "(A : 0) - (B : 1290) - (C : 515) - (D : 600)")

        b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
        c = ["A", "B"]
        TestCase().assertEqual(self.stock_list(b, c), "(A : 200) - (B : 1140)")


def main():
    print("Help the bookseller!")
    HelpTheBookseller().demo()
    HelpTheBookseller().test()


if __name__ == "__main__":
    main()

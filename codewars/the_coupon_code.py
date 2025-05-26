from datetime import datetime
from unittest import TestCase


class TheCouponCode(object):
    """https://www.codewars.com/kata/539de388a540db7fec000642/train/python"""
    def __init__(self):
        pass

    @staticmethod
    def check_coupon(entered_code, correct_code, current_date, expiration_date):
        get_date = lambda date_str: datetime.strptime(date_str, "%B %d, %Y")
        if (entered_code is not correct_code
                or get_date(current_date) > get_date(expiration_date)):
            return False
        return True
        # print(f"{entered_code=} {correct_code=} {current_date=} {expiration_date=}")

    def demo(self):
        print("Demo")
        print(f'{self.check_coupon("123", "123", "September 5, 2014", "October 1, 2014")=}')
        print(f'{self.check_coupon("123", "123", "September 5, 2014", "October 1, 2000")=}')
        print(f'{self.check_coupon("123a", "123", "September 5, 2014", "October 1, 2014")=}')
        print(f'{self.check_coupon(0, False, "September 5, 2014", "September 5, 2014")=}')
        print(f'{self.check_coupon(1, True, "September 5, 2014", "September 5, 2014")=}')

    def test(self):
        print("Tests")
        TestCase().assertEqual(self.check_coupon("123", "123", "September 5, 2014", "October 1, 2014"), True);
        TestCase().assertEqual(self.check_coupon("123a", "123", "September 5, 2014", "October 1, 2014"), False);


def main():
    print("The Coupon Code")
    TheCouponCode().demo()
    TheCouponCode().test()


if __name__ == "__main__":
    main()

import sys


def get_base_prefix_compat():
    """Get base/real prefix, or sys.prefix if there is none."""
    return getattr(sys, "base_prefix", None) or getattr(sys, "real_prefix", None) or sys.prefix

def in_virtualenv():
    return get_base_prefix_compat() != sys.prefix


class MathDemo(object):
    """Math Demonstration Class"""

    def __init__(self):
        pass

    def add(self, a, b):
        """
        Add :math:`a` and :math:`b` and return the result

        :math:`a + b`
        """
        return a + b


def main():
    print("Hello, World!")

    print(in_virtualenv())
    print(sys.prefix)

    math_demo = MathDemo()
    print(math_demo.add(3, 5))


if __name__ == "__main__":
    main()

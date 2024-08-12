def main():
    print("Stringsd Demo")

    a = 7
    b = 3.14
    c = 123456.789
    print("Normal print: ", a, b, c)
    print("C print: %d %f %.2f" % (a, b, c))
    print("Format print: {0} {1} {2}".format(a, b, c))
    print(f"F-string print: {a} {b=} {c=:,.2f}")
    print(f"F-string print of decimal number with leading zeroes: {a=:07d}")


if __name__ == "__main__":
    main()

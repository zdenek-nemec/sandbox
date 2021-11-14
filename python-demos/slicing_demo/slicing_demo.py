def main():
    print("Slicing Demo")

    text = "Python"  # text[start:stop:step]
    print("All:        %s" % text[:])
    print("First:      %s" % text[0])
    print("Last:       %s" % text[-1])
    print("First 3:    %s" % text[:3])
    print("Last 3:     %s" % text[-3:])
    print("3rd to end: %s" % text[2:])
    print("3rd to 4th: %s" % text[2:4])
    print("Every 2nd:  %s" % text[::2])
    print("Reversed:   %s" % text[::-1])


if __name__ == "__main__":
    main()

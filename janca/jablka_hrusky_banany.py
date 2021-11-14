BRAND_A = ["jablka", "hrusky"]
BRAND_B = ["jablka", "banany"]
BRAND_C = ["banany"]


def search_a(item):
    if item in BRAND_A:
        return True
    else:
        return False


def search_b(item):
    if item in BRAND_B:
        return True
    else:
        return False


def search_c(item):
    if item in BRAND_C:
        return True
    else:
        return False


def search(item, search_function):
    return search_function(item)


def main():
    print("Jablka, Hrusky, Banany")
    for search_function in [search_a, search_b, search_c]:
        print(search("jablka", search_function))


if __name__ == "__main__":
    main()

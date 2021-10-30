USAGE_VT = 2.398
USAGE_NT = 3.305

ELECTRICITY_OFFERS = [{
    "Dodavatel": "MND D25d 3x25 A",
    "Obchodni": {
        "Poplatky CZK/mesic": 77,
        "Elektrina VT CZK/MWh": 4875,
        "Elektrina NT CZK/MWh": 3818
    },
    "Regulovane": {
        "Distribuce VT CZK/MWh": 2080.72,
        "Distribuce NT CZK/MWh": 164.45,
        "Rezervovany prikon CZK/mesic": 164.56,
        "Systemove sluzby CZK/MWh": 112.89,
        "Podpora vykupu CZK/mesic": 0,
        "Podpora vykupu CZK/MWh": 598.95,
        "OTE CZK/mesic": 4.73,
        "Dan CZK/MWh": 34.24
    }
}, {
    "Dodavatel": "MND D26d 3x25 A",
    "Obchodni": {
        "Poplatky CZK/mesic": 77,
        "Elektrina VT CZK/MWh": 4875,
        "Elektrina NT CZK/MWh": 3818
    },
    "Regulovane": {
        "Distribuce VT CZK/MWh": 763.64,
        "Distribuce NT CZK/MWh": 164.45,
        "Rezervovany prikon CZK/mesic": 274.67,
        "Systemove sluzby CZK/MWh": 112.89,
        "Podpora vykupu CZK/mesic": 0,
        "Podpora vykupu CZK/MWh": 598.95,
        "OTE CZK/mesic": 4.73,
        "Dan CZK/MWh": 34.24
    }
}, {
    "Dodavatel": "E.ON D25d 3x25 A",
    "Obchodni": {
        "Poplatky CZK/mesic": 96,
        "Elektrina VT CZK/MWh": 4394,
        "Elektrina NT CZK/MWh": 3903
    },
    "Regulovane": {
        "Distribuce VT CZK/MWh": 2143.27,
        "Distribuce NT CZK/MWh": 178.95,
        "Rezervovany prikon CZK/mesic": 159,
        "Systemove sluzby CZK/MWh": 112.89,
        "Podpora vykupu CZK/mesic": 0,
        "Podpora vykupu CZK/MWh": 598.95,
        "OTE CZK/mesic": 4.73,
        "Dan CZK/MWh": 34.24
    }
}, {
    "Dodavatel": "E.ON D26d 3x25 A",
    "Obchodni": {
        "Poplatky CZK/mesic": 96,
        "Elektrina VT CZK/MWh": 4394,
        "Elektrina NT CZK/MWh": 3903
    },
    "Regulovane": {
        "Distribuce VT CZK/MWh": 775.63,
        "Distribuce NT CZK/MWh": 178.95,
        "Rezervovany prikon CZK/mesic": 288,
        "Systemove sluzby CZK/MWh": 112.89,
        "Podpora vykupu CZK/mesic": 0,
        "Podpora vykupu CZK/MWh": 598.95,
        "OTE CZK/mesic": 4.73,
        "Dan CZK/MWh": 34.24
    }
}]


def compare_electricity(offers, vt, nt):
    for item in offers:
        price_per_month = (
            item["Obchodni"]["Poplatky CZK/mesic"]
            + item["Regulovane"]["Rezervovany prikon CZK/mesic"]
            + item["Regulovane"]["OTE CZK/mesic"]
        )
        price_per_mwh_vt = (
            item["Obchodni"]["Elektrina VT CZK/MWh"]
            + item["Regulovane"]["Distribuce VT CZK/MWh"]
            + item["Regulovane"]["Systemove sluzby CZK/MWh"]
            + item["Regulovane"]["Podpora vykupu CZK/MWh"]
            + item["Regulovane"]["Dan CZK/MWh"]
        )
        price_per_mwh_nt = (
            item["Obchodni"]["Elektrina NT CZK/MWh"]
            + item["Regulovane"]["Distribuce NT CZK/MWh"]
            + item["Regulovane"]["Systemove sluzby CZK/MWh"]
            + item["Regulovane"]["Podpora vykupu CZK/MWh"]
            + item["Regulovane"]["Podpora vykupu CZK/mesic"]
            + item["Regulovane"]["Dan CZK/MWh"]
        )
        print(item["Dodavatel"])
        print("* Poplatky CZK/mesic: %f" % price_per_month)
        print("* VT CZK/MWh: %f" % price_per_mwh_vt)
        print("* NT CZK/MWh: %f" % price_per_mwh_nt)
        total_price_per_year = (
            12 * price_per_month
            + vt * price_per_mwh_vt
            + nt * price_per_mwh_nt
        )
        print("* Celkem za rok CZK: %f" % total_price_per_year)
        print("* Mesicni zalohy CZK: %f" % (total_price_per_year / 12))


def main():
    compare_electricity(ELECTRICITY_OFFERS, USAGE_VT, USAGE_NT)


if __name__ == "__main__":
    main()

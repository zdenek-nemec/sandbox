DEFAULT_USAGE_HIGH_TARIFF = 2.398
DEFAULT_USAGE_LOW_TARIFF = 3.305

ELECTRICITY_OFFERS = [
    {
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
    }
]


def compare_electricity(offer_list, usage_high_tariff, usage_low_tariff):
    for offer in offer_list:
        price_per_month = (
            offer["Obchodni"]["Poplatky CZK/mesic"]
            + offer["Regulovane"]["Rezervovany prikon CZK/mesic"]
            + offer["Regulovane"]["OTE CZK/mesic"]
        )
        price_per_mwh_high_tariff = (
            offer["Obchodni"]["Elektrina VT CZK/MWh"]
            + offer["Regulovane"]["Distribuce VT CZK/MWh"]
            + offer["Regulovane"]["Systemove sluzby CZK/MWh"]
            + offer["Regulovane"]["Podpora vykupu CZK/MWh"]
            + offer["Regulovane"]["Dan CZK/MWh"]
        )
        price_per_mwh_low_tariff = (
            offer["Obchodni"]["Elektrina NT CZK/MWh"]
            + offer["Regulovane"]["Distribuce NT CZK/MWh"]
            + offer["Regulovane"]["Systemove sluzby CZK/MWh"]
            + offer["Regulovane"]["Podpora vykupu CZK/MWh"]
            + offer["Regulovane"]["Podpora vykupu CZK/mesic"]
            + offer["Regulovane"]["Dan CZK/MWh"]
        )
        print(offer["Dodavatel"])
        print("* Poplatky CZK/mesic: %f" % price_per_month)
        print("* VT CZK/MWh: %f" % price_per_mwh_high_tariff)
        print("* NT CZK/MWh: %f" % price_per_mwh_low_tariff)
        total_price_per_year = (
            12 * price_per_month
            + usage_high_tariff * price_per_mwh_high_tariff
            + usage_low_tariff * price_per_mwh_low_tariff
        )
        print("* Celkem za rok CZK: %f" % total_price_per_year)
        print("* Mesicni zalohy CZK: %f" % (total_price_per_year / 12))


def main():
    print("Energy Supplier Comparison")
    compare_electricity(ELECTRICITY_OFFERS, DEFAULT_USAGE_HIGH_TARIFF, DEFAULT_USAGE_LOW_TARIFF)


if __name__ == "__main__":
    main()

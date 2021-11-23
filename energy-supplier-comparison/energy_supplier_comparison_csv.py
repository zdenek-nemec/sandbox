import csv

DEFAULT_OFFERS_FILE = "electricity_offers.csv"
DEFAULT_USAGE_HIGH_TARIFF = 1.5
DEFAULT_USAGE_LOW_TARIFF = 0.0


def get_offers_csv_list(offers_file):
    csv_list = []
    with open(offers_file, "r") as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        for row in reader:
            csv_list.append(row)
    return csv_list


def initialise_offers_list(csv_list):
    offer_list = []
    for index, field in enumerate(csv_list[0]):
        if field in ["Polozka", "Uctovani"]:
            continue
        else:
            offer_list.append({
                "Dodavatel": field,
                "Sloupec": index
            })
    return offer_list


def load_offer(offer, csv_list):
    column = offer["Sloupec"]
    for csv_entry in csv_list[1:]:
        item = csv_entry[0]
        unit = csv_entry[1]
        if unit not in offer:
            offer[unit] = {}
        offer[unit][item] = csv_entry[column]


def get_offers_json_list(csv_list):
    offer_list = initialise_offers_list(csv_list)
    for index in range(len(offer_list)):
        offer = offer_list.pop(0)
        load_offer(offer, csv_list)
        offer_list.append(offer)
    return offer_list


def get_offers(offers_file):
    offers_csv_list = get_offers_csv_list(offers_file)
    offers_json_list = get_offers_json_list(offers_csv_list)
    return offers_json_list


def compare_offers(offer_list, usage_high_tariff, usage_low_tariff):
    for offer in offer_list:
        price_per_month = sum([float(value) for value in offer["Mesic"].values()])
        price_per_mwh_high_tariff = sum([float(offer["MWh"][key]) for key in offer["MWh"].keys() if key[-2:] != "NT"])
        price_per_mwh_low_tariff = sum([float(offer["MWh"][key]) for key in offer["MWh"].keys() if key[-2:] != "VT"])
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
    print("Energy Supplier Comparison - CSV")
    offers = get_offers(DEFAULT_OFFERS_FILE)
    compare_offers(offers, DEFAULT_USAGE_HIGH_TARIFF, DEFAULT_USAGE_LOW_TARIFF)


if __name__ == "__main__":
    main()

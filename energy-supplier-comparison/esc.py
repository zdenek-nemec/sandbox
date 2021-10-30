import csv

DEFAULT_OFFERS_FILE = "electricity_offers.csv"


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
        if field in ["Typ", "Polozka", "Uctovani"]:
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
        item = csv_entry[1]
        unit = csv_entry[2]
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


def main():
    print("Energy Supplier Comparison")
    offers = get_offers(DEFAULT_OFFERS_FILE)
    [print(offer) for offer in offers]


if __name__ == "__main__":
    main()

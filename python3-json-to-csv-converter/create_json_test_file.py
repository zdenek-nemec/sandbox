import json


def create_data():
    return [{
        "record_id": 1,
        "calling_msisdn": "+420731000001",
        "called_msisdn": "+420731000002",
        "calling_imsi": "230010000000001",
        "called_imsi": "230010000000002",
        "calling_operator": "T-Mobile CZ",
        "called_operator": "T-Mobile CZ",
        "start_time": "2020-07-18 11:47:00.123",
        "end_time": "2020-07-18 11:48:30.123",
        "call_duration_ms": 90000
    }, {
        "record_id": 2,
        "calling_msisdn": "+420731000002",
        "called_msisdn": "+420721000003",
        "calling_imsi": "230010000000002",
        "calling_operator": "T-Mobile CZ",
        "called_operator": "O2 CZ",
        "start_time": "2020-07-18 11:50:00.123",
        "end_time": "2020-07-18 11:55:00.123",
        "call_duration_ms": 300000
    }]


def create_json_test_file():
    with open("test_data.json", "w", encoding="utf-8") as json_file:
        json.dump(create_data(), json_file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    create_json_test_file()

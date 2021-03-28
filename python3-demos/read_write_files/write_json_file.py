import json


DEFAULT_FILENAME = "output_test_file.json"
DEFAULT_CONTENT = [
    {
        "record_id": 1,
        "calling": {
            "imsi": "230010000000001",
            "msisdn": "+420731000001",
            "operator": "T-Mobile CZ",
        },
        "called": {
            "imsi": "230010000000002",
            "msisdn": "+420731000002",
            "operator": "T-Mobile CZ",
        },
        "start_time": "2020-07-18 11:47:00.123",
        "end_time": "2020-07-18 11:48:30.123",
        "call_duration_ms": 90000
    }, {
        "record_id": 2,
        "calling": {
            "imsi": "230010000000002",
            "msisdn": "+420731000002",
            "operator": "T-Mobile CZ",
        },
        "called": {
            "msisdn": "+420721000003",
            "operator": "O2 CZ",
        },
        "start_time": "2020-07-18 11:50:00.123",
        "end_time": "2020-07-18 11:55:00.123",
        "call_duration_ms": 300000
    }
]


def main():
    filename = DEFAULT_FILENAME
    content = DEFAULT_CONTENT;
    with open(filename, "w", encoding="utf-8") as json_file:
        json.dump(content, json_file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    main()

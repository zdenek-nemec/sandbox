import datetime
import random


DAYS_TO_GENERATE = 10


def generate_random_data(entries):
    timestamps = [(datetime.datetime.strptime("2021-05-01 0:00:00", "%Y-%m-%d %H:%M:%S") + datetime.timedelta(hours=x)) for x in range(entries)]
    values = random.sample(range(0,1000), entries)
    return [(timestamps[i], values[i]) for i in range(entries)]


def main():
    print("Hello, Adaptive Statistics Alarm!")

    data = generate_random_data(DAYS_TO_GENERATE * 24)
    # for entry in data:
    #     print(entry[0].strftime("%Y-%m-%d %H:%M:%S"), ",", entry[1], sep="")

    # Save random data to CSV

    # Load data from CSV

    # Best match data timestamps

    # Calculate variance

    # Alarm if variance raises too much


if __name__ == "__main__":
    main()

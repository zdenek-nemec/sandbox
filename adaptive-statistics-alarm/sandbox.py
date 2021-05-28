import datetime
import random
import statistics


DAYS_TO_GENERATE = 10


def generate_random_data(entries):
    timestamps = [(datetime.datetime.strptime("2021-05-01 0:00:00", "%Y-%m-%d %H:%M:%S") + datetime.timedelta(hours=x)) for x in range(entries)]
    values = random.sample(range(0,1000), entries)
    return [(timestamps[i], values[i]) for i in range(entries)]


def get_time_of_day_data(data):
    todd = {}
    for entry in data:
        hour = entry[0].strftime("%H")
        if hour in todd:
            todd[hour].append((entry[0].strftime("%Y-%m-%d"), entry[1]))
        else:
            todd[hour] = [(entry[0].strftime("%Y-%m-%d"), entry[1])]
    return todd


def get_todd_with_variance(todd):
    toddv = {}
    for hour in todd.keys():
        for index, entry in enumerate(sorted(todd[hour])):
            if index == 0:
                toddv[hour] = [(entry[0], entry[1], 0)]
            else:
                processed = [x[1] for x in toddv[hour]]
                toddv[hour].append((entry[0], entry[1], statistics.pvariance(processed + [entry[1]])))
    return toddv


def main():
    print("Hello, Adaptive Statistics Alarm!")

    data = generate_random_data(DAYS_TO_GENERATE * 24)
    # for entry in data:
    #     print(entry[0].strftime("%Y-%m-%d %H:%M:%S"), ",", entry[1], sep="")

    # Save random data to CSV

    # Load data from CSV

    todd = get_time_of_day_data(data)
    # print(todd)
    # [print(x) for x in sorted(todd["10"])]

    toddv = get_todd_with_variance(todd)
    # print(toddv)
    # [print(x) for x in sorted(toddv["10"])]

    # Alarm if variance raises too much


if __name__ == "__main__":
    main()

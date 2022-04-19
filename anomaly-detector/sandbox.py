import datetime
import random
import statistics


DAYS_TO_GENERATE = 31


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


def get_todd_with_parameter(todd, function):
    toddv = {}
    for hour in todd.keys():
        for index, entry in enumerate(sorted(todd[hour])):
            if index == 0:
                toddv[hour] = [(entry[0], entry[1], 0)]
            else:
                processed = [x[1] for x in toddv[hour]]
                toddv[hour].append((entry[0], entry[1], function(processed + [entry[1]])))
    return toddv


def alarm_when_parameter_raises(data):
    for hour in sorted(data.keys()):
        print("Hour", hour)
        for index, entry in enumerate(sorted(data[hour])):
            if index in [0, 1]:
                print("          ", entry[0], entry[1])
                last_parameter = entry[2]
            elif entry[2] > last_parameter:
                print("    alarm ", entry[0], entry[1])
                last_parameter = entry[2]
            else:
                print("          ", entry[0], entry[1])
                last_parameter = entry[2]


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

    # toddv = get_todd_with_parameter(todd, lambda data : statistics.pvariance(data))
    # print(toddv)
    # [print(x) for x in sorted(toddv["10"])]

    toddd = get_todd_with_parameter(todd, lambda data : statistics.pstdev(data))
    # print(toddd)
    # [print(x) for x in sorted(toddd["10"])]

    # print("Variance")
    # alarm_when_parameter_raises(toddv)
    print("Deviance")
    alarm_when_parameter_raises(toddd)


if __name__ == "__main__":
    main()

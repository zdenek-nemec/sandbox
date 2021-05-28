def generate_random_data(filename, entries):
    data = []
    for i in range(0, entries):
        data.append((i, 0))
    return data


def main():
    print("Hello, Adaptive Statistics Alarm!")

    data = generate_random_data("random_data_sample.csv", 10)
    print(data)

    # Generate random data with timestamps

    # Save random data to CSV

    # Load data from CSV

    # Best match data timestamps

    # Calculate variance

    # Alarm if variance raises too much


if __name__ == "__main__":
    main()

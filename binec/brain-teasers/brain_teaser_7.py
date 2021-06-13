# Find numbers represented as sum of two cubes for two different pairs


N = 100000


def main():
    cubes = {}
    for i in range(1, N):
        cubes[i] = i ** 3
    sums = {}
    for i1 in cubes:
        for i2 in cubes:
            if i1 == i2:
                continue
            cube_sum = cubes[i1] + cubes[i2]
            if cube_sum > N:
                break
            numbers = sorted([i1, i2])
            if cube_sum in sums:
                if numbers in sums[cube_sum]:
                    continue
                sums[cube_sum].append(numbers)
            else:
                sums[cube_sum] = [numbers]
    for item in sums:
        if len(sums[item]) > 1:
            print(item, sums[item])


if __name__ == '__main__':
    main()

# Perform Division of two numbers without using division operator

def main():
    a = -7
    b = 1.6

    sign = '-'
    if (a >= 0 and b >= 0) or (a < 0 and b < 0):
        sign = '+'
    a = abs(a)
    b = abs(b)

    result = []
    rest = a
    while True:
        if a == 0 or b == 0:
            result.append('0')
            break
        elif rest == 0 or len(result) > 10:
            break
        number = 0
        while True:
            if rest >= b:
                number += 1
                rest -= b
            else:
                break
        result.append(str(number))
        if len(result) == 1:
            result.append('.')
        rest *= 10
    result = [sign] + result
    result = float(''.join(result))
    print(result)


if __name__ == '__main__':
    main()

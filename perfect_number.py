def is_perfect(number):
    factor = [i for i in range(1, number) if not number % i]
    return sum(factor) == number and number != 0

if __name__ == '__main__':
    print is_perfect(6)

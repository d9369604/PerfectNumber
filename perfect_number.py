def is_perfect(number):

    number = int(number)

    if number <= 0:
        raise Exception('please enter positive number')

    factor = [i for i in range(1, number) if not number % i]
    return sum(factor) == number

if __name__ == '__main__':
    print is_perfect(6)

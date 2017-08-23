def is_perfect(number):
    # number = int(number)
    factor = [i for i in range(1, number) if not number % i]
    return True if sum(factor) == number else False

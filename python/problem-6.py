def sum_of_squares(value):
    sum = 0
    for _ in range(value + 1):
        sum = sum + _ ** 2

    return sum


def summed_squares(value):
    sum = 0
    for _ in range(value + 1):
        sum += _

    return sum ** 2


print(summed_squares(100) - sum_of_squares(100))
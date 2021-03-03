import math


def check_if_factor(guess, value):
    """Check if the guess is a factor of the value"""
    if value % guess == 0:
        return True
    else:
        return False


def check_if_prime(value):
    """Check if the value is a prime number"""
    for _ in range(2, value):
        if value % _ == 0:
            return False

    return True


i = 600851475143
j = 1
largest_factor = 0

while j < math.sqrt(i):
    if check_if_factor(j, i):
        if check_if_prime(j):
            largest_factor = j
            print(largest_factor)
    j += 2

print(f"Answer: {largest_factor}")
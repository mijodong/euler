from math import floor


def is_palindrome(value):
    value_str = str(value)
    length = len(value_str)

    for i in range(floor(length / 2)):
        if value_str[i] != value_str[-i - 1]:
            return False

    return True


palindrome = 0

for i1 in range(100, 999):
    for i2 in range(100, 999):
        quotient = i1 * i2
        if is_palindrome(quotient):
            if quotient > palindrome:
                palindrome = quotient

print(palindrome)
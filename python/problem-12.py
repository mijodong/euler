i = 1
divisors = []
while len(divisors) < 200:
    divisors[:] = []
    triangle_number = 0
    for _ in range(1, i):
        triangle_number += _

    for _ in range(1, triangle_number + 1):
        if triangle_number % _ == 0:
            divisors.append(_)

    # print(triangle_number, divisors)
    i += 1

print(i, triangle_number, divisors)

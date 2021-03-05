def check_if_prime(value):
    """Check if the value is a prime number"""
    for _ in range(2, value):
        if value % _ == 0:
            return False

    return True


primes = []
i = 1

while len(primes) < 10001:
    if check_if_prime(i):
        primes.append(i)

    i += 2

print(primes)
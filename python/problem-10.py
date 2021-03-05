from math import sqrt, floor

# Create sieve
max_value = 2000000
sieve = []

for _ in range(max_value):
    sieve.append(True)

for i in range(2, int(round(sqrt(max_value)))):
    if sieve[i]:
        for j in range(i ** 2, max_value, i):
            sieve[j] = False

total = 0
for i in range(2, len(sieve)):
    if sieve[i]:
        total += i

print(total)
import math

checksum = 1000

for a in range(1, checksum):
    for b in range(1, checksum):
        c = math.sqrt(a ** 2 + b ** 2)
        if a + b + c == checksum:
            answer = a * b * c

print(answer)
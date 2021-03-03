i1 = 0
i2 = 1
i3 = 0
sum = 0

while i1 < 4000000:
    i3 = i1 + i2
    i1 = i2
    i2 = i3
    if i1 % 2 == 0:
        sum += i1

print(sum)
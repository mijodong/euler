factorial = 1
for _ in range(1, 101):
    factorial *= _

value_sum = 0
for _ in str(factorial):
    value_sum += int(_)

print(value_sum)
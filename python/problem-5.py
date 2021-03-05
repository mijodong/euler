def smallest_multiple(value):
    for _ in range(20, 2, -1):
        if value % _ != 0:
            return False

    print(f"{value} is the smallest multiple.")
    return True


i = 20

while not smallest_multiple(i):
    i += 20
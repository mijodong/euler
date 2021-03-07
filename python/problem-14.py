starting_number = 999999
n = starting_number
counter = 1
largest_starting_number = 1
longest_chain = 1

while starting_number > 1:

    if n > 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
        counter += 1

    else:
        if counter > longest_chain:
            longest_chain = counter
            largest_starting_number = starting_number

        starting_number -= 1
        n = starting_number
        counter = 1

print(longest_chain, largest_starting_number)

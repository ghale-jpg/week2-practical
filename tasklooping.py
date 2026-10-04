numbers = [2, -3, 4, -5, -6, 7, 8, -9]

count = 0

for number in numbers:
    if number < 0:
        count += 1

print("Number of negative numbers:", count)
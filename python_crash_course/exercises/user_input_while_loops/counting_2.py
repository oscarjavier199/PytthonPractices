#program prints the odd numbers in a given range

current_number = 0

while current_number < 20:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
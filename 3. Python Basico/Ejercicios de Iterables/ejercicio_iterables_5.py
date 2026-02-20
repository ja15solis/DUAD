
all_numbers = []
counter = 0
while counter < 10:
    if counter == 0:
        all_numbers.append(float(input("Please enter the first number: ")))
    else: 
        all_numbers.append(float(input("Please enter the next number: ")))
    counter = counter + 1

print(f'The max number entered is {max(all_numbers)}')
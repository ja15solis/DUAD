my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,13,13,13,13]
pair_numbers = []
for index,value in enumerate(my_list):
    if value % 2 != 0:
        continue
    else:
        pair_numbers.append(value)

pair_numbers

print(pair_numbers)


list_of_numbers = [10,11,12] 

def sum_of_list_values(list):
    result = 0 
    for value in list:
        result += value
    return result


print(sum_of_list_values(list_of_numbers))
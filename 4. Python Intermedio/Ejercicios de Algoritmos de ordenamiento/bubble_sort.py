def bubble_sort(list):
    for external_index in range(0,len(list)-1):
        changes = False
        for internal_index in range(0,len(list)-1-external_index):
            current_value = list[internal_index]
            next_value = list[internal_index+1]
            print(f"Iteration {external_index}.{internal_index}, current value = {current_value}, next value = {next_value}")
            if current_value > next_value:
                list[internal_index] = next_value
                list[internal_index+1] = current_value
                print(f"Change made: {current_value} > {next_value}")
                changes = True
        if changes == False:
            return 

list_of_numbers = [1,5,20,7,9,11,15,16]
bubble_sort(list_of_numbers)
print(list_of_numbers)
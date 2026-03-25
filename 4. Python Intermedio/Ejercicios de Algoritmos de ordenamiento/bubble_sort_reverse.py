def bubble_sort(list):
    for external_index in range(0,len(list)-1):
        changes = False
        for internal_index in range(len(list)-1-external_index,0,-1):
            current_value = list[internal_index]
            prev_value = list[internal_index-1]
            print(f"Iteration {external_index}.{internal_index}, current value = {current_value}, previous value = {prev_value}")
            if current_value < prev_value:
                list[internal_index] = prev_value
                list[internal_index-1] = current_value
                print(f"Change made: {current_value} < {prev_value}")
                changes = True
        if changes == False:
            return 

list_of_numbers = [5,4,7,9,11,15,16,2]
bubble_sort(list_of_numbers)
print(list_of_numbers)
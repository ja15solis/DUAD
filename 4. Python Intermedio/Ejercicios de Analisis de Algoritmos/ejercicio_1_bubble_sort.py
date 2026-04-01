def bubble_sort(list): 
    for external_index in range(0,len(list)-1): # O(n)
        changes = False # O(1)
        for internal_index in range(0,len(list)-1-external_index): # O(n^2)
            current_value = list[internal_index] # O(1)
            next_value = list[internal_index+1] # O(1)
            print(f"Iteration {external_index}.{internal_index}, current value = {current_value}, next value = {next_value}") # O(1)
            if current_value > next_value: # O(1) 
                list[internal_index] = next_value # O(1)
                list[internal_index+1] = current_value # O(1)
                print(f"Change made: {current_value} > {next_value}") # O(1)
                changes = True # O(1)
        if changes == False: # O(1)
            return # O(1)

list_of_numbers = [1,5,20,7,9,11,15,16] 
bubble_sort(list_of_numbers) # O(n^2)
print(list_of_numbers) # O(1)
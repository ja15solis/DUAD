def bubble_sort(list_num):
    if not isinstance(list_num, list):
        raise TypeError
    for external_index in range(0,len(list_num)-1):
        changes = False
        for internal_index in range(0,len(list_num)-1-external_index):
            current_value = list_num[internal_index]
            next_value = list_num[internal_index+1]
            # print(f"Iteration {external_index}.{internal_index}, current value = {current_value}, next value = {next_value}")
            if current_value > next_value:
                list_num[internal_index] = next_value
                list_num[internal_index+1] = current_value
                # print(f"Change made: {current_value} > {next_value}")
                changes = True
        if changes == False:
            return list_num
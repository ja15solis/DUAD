test_list=[1,2,3,4,5,6,7,8,9,10,11,12,13]

last_value = test_list.pop(len(test_list)-1)
test_list.append(test_list[0])
#test_list.pop(test_list[0]) it doesn't work because the parameter is the index of the list so lest_list[0] = 1
test_list.pop(0)
test_list.insert(0,last_value)

print (test_list)

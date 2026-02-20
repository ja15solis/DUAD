test="hello world!"


def reverse_text(list):
    reversed_text=""
    for i in range(len(list)-1,-1,-1):
        reversed_text+= list[i] 
    
    return reversed_text


print(reverse_text(test))
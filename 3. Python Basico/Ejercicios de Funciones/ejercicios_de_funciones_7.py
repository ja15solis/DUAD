import math

def is_prime(number):
    if number < 0:
        return is_prime(number*-1)
    elif number < 1:
        return False
    elif (number ==1 or number ==2):
        return True
    else:
        for i in range (1,math.floor(math.sqrt(number))+1,1): ## previous int number of square root of the number (+1 because it doesn't use the upper limit)
            if i ==1:
                continue
            elif number % i == 0 :
                return False
            else:
                continue
        return True


def prime_numbers_within_a_list(list):
    prime_numbers=[]
    for value in list:
        if is_prime(value):
            prime_numbers.append(value)
    return prime_numbers

list_of_numbers= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(prime_numbers_within_a_list(list_of_numbers))

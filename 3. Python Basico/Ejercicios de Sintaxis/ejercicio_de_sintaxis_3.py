import random
secret_num = random.randint(1, 10)

user_input = int(input("Guess the secret number from 1 to 10: "))

while user_input != secret_num :
    user_input = int(input("Wrong number, try again: "))

print( f'Right, the correct number is {secret_num}')

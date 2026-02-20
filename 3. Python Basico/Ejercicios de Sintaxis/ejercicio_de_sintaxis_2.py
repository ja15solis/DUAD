# bebé, niño, preadolescente, adolescente, adulto joven, adulto, o adulto mayor

first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")
age = int(input("Please enter your age: "))
if age <=0:
    print("Please enter a positive number")
elif age < 1.5:
    stage =  "a baby"
elif age < 10 :
    stage =  "a child"
elif age < 12:
    stage =  "a preadolescent"
elif age< 21:
    stage =   "a teenager"
elif age < 40:
    stage =  "a young adult"
elif age < 65:
    stage =   "an adult"
else:
    stage =  "an older adult"

print(f'{first_name} {last_name}, you are {stage}')

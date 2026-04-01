import datetime


def get_difference_years(start_date, end_date):
    #this creates a tuple for month and dates and creates a comparison with each one month and day (If true then 1 if not then 0)
    diff = start_date.year - end_date.year - ((start_date.month, start_date.day) < (end_date.month, end_date.day)) 
    return diff


class User():
    def __init__(self,name,date_of_birth):
        self.name = name
        self.date_of_birth = datetime.date.fromisoformat(date_of_birth) #Specifying the format of the date (iso format) if I use the inheritance this will already be a datetime.date instance
    
    @property
    def age (self):
        current_dt = datetime.date.today()
        return get_difference_years(current_dt,self.date_of_birth)

def is_under_age(func):
    def wrapper (user_object,*args): #user object
        if user_object.age < 18:
            return "The account can't be created, is underage"
        else: 
            return func(user_object,*args)
    return wrapper # if you dont put this return wrapper the decorator returns None

@is_under_age
def create_account(user): # User the class
    return (f"Account created successfully for {user.name}" )

print("-" * 47)
print("Example underage:")
print(" - " * 16)
javier = User("Javier",'2009-01-22')
account_javier = create_account(javier)
print(account_javier)


print("-" * 47)
print("Example acceptable:")
print(" - " * 16)
amanda = User("Amanda",'2003-01-22')
account_amanda = create_account(amanda)
print(account_amanda)

# 2.1 scope with inside variable
def print_name():
    name = "javier"
    print(name)

#print(name) #error name is not defined


# 2.2 scope with outside variable
last_name = "solis"

def print_last_name():
    last_name = "jimenez" 
    print(last_name)

print_last_name()
print (last_name)

#changes only for the function and it doesn't change the original value of "last_name"
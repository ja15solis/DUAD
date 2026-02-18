user = {
    'first_name': 'javier',
    'last_name': 'solis', 
    'email': 'ja15.solis@gmail.com', 
    'favorite_color': 'blue',
    'age': 28 ,
    'place of birth': 'San José, Costa Rica'
    }

keys_to_eliminate = ['age','place','place of birth']

for index in range(len(keys_to_eliminate)):
    eliminated_value = user.pop(keys_to_eliminate[index],None) #none is a parameter used for handling keys that doesn't exist in a dict
    if eliminated_value is None:
        print(f'The key "{keys_to_eliminate[index]}" was not found')
    else:
        print(f'The key "{keys_to_eliminate[index]}" was eliminated from user')

print(user)
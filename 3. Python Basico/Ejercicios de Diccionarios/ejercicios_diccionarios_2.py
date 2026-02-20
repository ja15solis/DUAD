keys = ['first_name', 'last_name', 'email', 'favorite_color']
values = ['javier', 'solis', 'ja15.solis@gmail.com', 'blue']

user = {keys[x]:values[x] for x in range(len(keys))}

print(user)

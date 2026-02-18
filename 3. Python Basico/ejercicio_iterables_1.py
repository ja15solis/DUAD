albums = ["Bocanada","MTV Unplugged in New York","I'm with you", "The Color and the Shape","Meteora"]
artist = ["Gustavo Cerati","Nirvana","Red Hot Chili Peppers","Foo Fighters","Linkin Park"]

print("Album and artist: ")

for index, album in enumerate(albums):
    print(f'{album} - {artist[index]}' )

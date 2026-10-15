import hashlib

# encode() convierte el string a bytes, que es lo que el algoritmo necesita recibir
print(hashlib.md5("lyfter123".encode()).hexdigest())
print(hashlib.md5("Lyfter22sfadfasdf3".encode()).hexdigest())
print(hashlib.md5("Lyfter22sfadfasdf3".encode()).hexdigest())
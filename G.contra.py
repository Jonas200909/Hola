import random
caracteres="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
longitud=int(input("Ingresa la longitud de tu contraseña: "))
resultado=""
for i in range(longitud):
    resultado+=random.choice(caracteres)

print(f"Tu contraseña con una longitud {longitud} es: {resultado}")
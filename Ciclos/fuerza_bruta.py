from string import ascii_lowercase
import getpass

pwd = getpass.getpass("Ingrese la contraseña: ")

contador = 0

for i in pwd:
    for j in ascii_lowercase:
        contador = contador + 1
        if i == j:
            break

print(f"La contraseña fue forzada en {contador} intentos")
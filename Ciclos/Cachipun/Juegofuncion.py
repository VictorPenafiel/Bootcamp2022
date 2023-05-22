import random
import sys
from enum import Enum

class Opcion(Enum):
    PIEDRA = "piedra"
    PAPEL = "papel"
    TIJERA = "tijera"

def obtener_opcion_usuario():
    opcion = input("Ingrese una opción (piedra, papel, tijera): ")
    try:
        return Opcion(opcion.lower())
    except ValueError:
        print("Opción inválida: Debe ser piedra, papel o tijera")
        return obtener_opcion_usuario()

def determinar_ganador(opcion_usuario, opcion_computadora):
    if opcion_usuario == opcion_computadora:
        return "Empate"
    elif (opcion_usuario == Opcion.PIEDRA and opcion_computadora == Opcion.TIJERA) or \
         (opcion_usuario == Opcion.PAPEL and opcion_computadora == Opcion.PIEDRA) or \
         (opcion_usuario == Opcion.TIJERA and opcion_computadora == Opcion.PAPEL):
        return "Ganaste"
    else:
        return "Perdiste"

def jugar():
    opcion_usuario = obtener_opcion_usuario()
    opcion_computadora = random.choice(list(Opcion))
    print('Tu jugaste', opcion_usuario.value)
    print('Computador jugó', opcion_computadora.value)
    resultado = determinar_ganador(opcion_usuario, opcion_computadora)
    print(resultado)

if __name__ == "__main__":
    jugar()

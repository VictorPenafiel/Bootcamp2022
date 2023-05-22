import random
import sys

opcion = sys.argv[1]

jugadas = ['piedra','papel', 'tijera']

jugada_comp = random.choice(jugadas)

if opcion != "piedra" and opcion != "papel" and opcion != "tijera":
    print ("Argumento inválido: Debe ser piedra, papel o tijera")

else:
    print('Tu jugaste', opcion)
    print('Computador jugó', jugada_comp)

    if (opcion =='piedra' and jugada_comp == 'tijera') or \
        (opcion =='papel' and jugada_comp == 'piedra') or \
        (opcion =='tijera' and jugada_comp == 'papel'):
            print('Ganaste!!')
    elif opcion == jugada_comp:
        print('Empate!')
    else:
        print('Perdiste!!')
    

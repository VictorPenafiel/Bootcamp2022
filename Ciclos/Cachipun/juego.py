""" Codificar un programa en Python utilizando instrucciones de bloque para manejar el flujo en base a condiciones lógicas.
Descripción: Cachipún, también conocido como chin chan pu, pikachú, jankenpón, yan ken po, pin pon papas, hakembó o how-are-you-speak, es un juego de manos con tres elementos: la piedra vence a las tijeras rompiéndolas, las tijeras vencen al papel cortándolo y el papel vence a la piedra envolviéndola, formando un círculo o ciclo cerrado. A menudo se utiliza para decidir cuál de dos personas hará algo, similar a lanzar una moneda o para resolver un asunto.

Para poner en práctica lo que hemos aprendido a lo largo de la unidad, implementaremos un programa en Python que te permita jugar cachipún contra el ordenador.

Requisitos:

Crear el programa cachipun.py donde el usuario proporcionará piedra, papel o tijera como argumento. El ordenador elegirá un valor aleatorio. Para ello, investiga random.choice() de la biblioteca random. (2 Puntos)
El programa se ejecutará de la siguiente manera: python juego.py piedra Jugaste Piedra El ordenador jugó Tijera ¡Ganaste!

Considera las opciones de ganar, perder o empatar con el ordenador.
Si el argumento es diferente de piedra, papel o tijera, el programa debe mostrar las opciones que se pueden jugar.
python juego.py papelon 
Argumento inválido: Debe ser piedra, papel o tijera.
 """


import random
import sys

opcion = sys.argv[1]    #Opcion de jugador  por teclado. 
                        #python juego.py piedra

jugadas = ['piedra','papel', 'tijera'] #Lista de jugadas

jugada_comp = random.choice(jugadas) #Jugada aleatoria usando la biblioteca random.choice()

if opcion != "piedra" and opcion != "papel" and opcion != "tijera": # Si la opcion es diferente de piedra, papel o tijera,
    print ("Argumento inválido: Debe ser piedra, papel o tijera")   #Se imprimirá el mensaje de error

else:   #Si no "de lo contrario", se muestra la opción que se ha jugado el jugador y el computador
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

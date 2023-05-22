""" El IMC, conocido también como el Índice de masa corporal, es una medida que asocia el peso de una persona con su talla (su altura). Este valor es utilizado normalmente como un indicador nutricional y constituye un índice fácil y sencillo de calcular para determinar el estado de obesidad y sobrepeso de una persona. El IMC se calcula de la siguiente manera:

IMC = peso / (altura * altura)

Para ello, la Organización Mundial de la Salud (OMS) ha determinado una clasificación así para distintos rangos de valores.
IMC Clasificación OMS
< 18.5 Bajo Peso
[ 18.5, 25 [ Adecuado
[ 25, 30 [ Sobrepeso
[ 30, 35[ Obesidad Grado I
[ 35, 40 [ Obesidad Grado II
< 40 Obesidad Grado III
En busca de mejorar la salud nutricional de los pacientes, se le solicita a usted como programador el hecho de diseñar una herramienta que permita determinar el estado nutricional de una persona.
Requerimientos
Se solicita crear el programa imc.py que permita calcular el IMC de una persona.
1. Al programa se debe ingresar el peso en Kg y la talla (altura) en centímetros.
2. Calcular el IMC ajustando los valores de entrada a las unidades requeridas por la fórmula. El resultado se debe informar con 2 decimales.
3. Entregar al usuario una salida acorde que permita conocer el valor de su IMC además de la clasificación dada por la OMS.
A modo de validación se entregan los siguientes valores para revisar su código:
python imc.py 81 178
Su IMC es 25.56
La clasificación OMS es Sobrepeso

 """

import sys

peso = float(sys.argv[1])
altura = float(sys.argv[2])

altura = altura/100
imc = peso/(altura**2)

print (f'Su IMC es {imc:.2f}\nLa clasificación OMS es') 

if imc <18.5:
    print('Bajo de Peso')
elif imc >18.5 and imc<25:
    print('Adecuado')
elif imc >25 and imc<30:
    print('Sobrepeso')
elif imc >30 and imc<35:
    print('Obesidad Grado I')
elif imc >35 and imc<40:
    print('Obesidad Grado II')
else:
    print('Obesidad Grado III')

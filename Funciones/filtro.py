import sys

def filtrar(diccionario, umbral, orden = 'mayor'):
    if orden == 'mayor':
        filtro = {k:v for k,v in diccionario.items() if v > umbral}
    elif orden == 'menor':
        filtro = {k:v for k,v in diccionario.items() if v < umbral}
    else:
        filtro = ''
    return filtro

precios = {'Notebook': 700000,
'Teclado': 25000,
'Mouse': 12000,
'Monitor': 250000,
'Escritorio': 135000,
'Tarjeta de Video': 1500000}

if len(sys.argv) == 1:
    print('Faltan argumentos')
else:
    if len(sys.argv) == 2:
        umbral = int(sys.argv[1])
        resultado = filtrar(precios,umbral)
        print(f"Los productos mayores al umbral son {', '.join(resultado)}")
    else:
        umbral = int(sys.argv[1])
        orden = sys.argv[2]
        resultado = filtrar(precios,umbral,orden)
        if resultado == '':
            print("Lo sentimos, no es una operacion valida")
        else:
            print(f"Los productos menores al umbral son {', '.join(resultado)}")
            
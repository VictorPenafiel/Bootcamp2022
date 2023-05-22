def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact

def productoria(lista):
    prod = 1
    for i in lista:
        prod = prod * i
    return prod

def calcular(**kwargs):
    parametros = kwargs.items()

    for item in parametros:
        if 'fact' in item[0]:
            f = factorial(item[1])
            print(f"El factorial de {item[1]} es {f}")
        elif  'prod' in item[0]:
            p = productoria(item[1])
            print(f"La productoria de {item[1]} es {p}")
        else:
            print("operacion no valida")

calcular(fact_1 = 5, prod_1 = [3,6,4,2,8], fact_2 = 6, prod_2 =[4,6,7,4,3])

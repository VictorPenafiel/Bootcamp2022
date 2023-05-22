import sys

def main(umbral):
    ventas = {
        "Enero": 15000,
        "Febrero": 22000,
        "Marzo": 12000,
        "Abril": 17000,
        "Mayo": 81000,
        "Junio": 13000,
        "Julio": 21000,
        "Agosto": 41200,
        "Septiembre": 25000,
        "Octubre": 21500,
        "Noviembre": 91000,
        "Diciembre": 21000,
    }

    filtro = {k: v for k, v in ventas.items() if v > umbral}
    print(filtro)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        umbral = int(sys.argv[1])
        main(umbral)
    else:
        print("Error - Introduce los argumentos correctamente")
        print("Ejemplo: python script.py 20000")



"""Para mejorar el código proporcionado, primero vamos a agregar una comprobación de seguridad para asegurarnos de que se proporciona un argumento antes de ejecutar el script. Además, se puede agregar un mensaje de error para informar al usuario de cómo utilizar el script correctamente en caso de que no se proporcione un argumento. También se puede utilizar una función main() para organizar el código de manera más estructurada docs.hektorprofe.net, programmerclick.com.



En esta versión mejorada, se ha movido el código principal a la función main(), que toma el valor de umbral como argumento. La comprobación de seguridad se realiza al verificar si len(sys.argv) == 2, lo que significa que se ha proporcionado un argumento adicional además del nombre del script. Si no se proporciona un argumento, se imprime un mensaje de error para guiar al usuario en cómo utilizar el script correctamente.

Esta estructura hace que el código sea más fácil de mantener y de leer, además de proporcionar un manejo adecuado de los casos en los que no se proporcionan argumentos.
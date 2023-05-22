CD import sys
umbral =int(sys.argv[1])


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

filtro = {k:v for k,v in ventas.items() if v >umbral}
print(filtro)

"""El código proporcionado funciona correctamente si se ejecuta desde la línea de comandos con un argumento numérico adecuado. Aquí hay una explicación detallada de cómo funciona el código:

    El módulo sys es importado para acceder a sys.argv, que es una lista que contiene todos los argumentos de la línea de comandos pasados al script en Python. En este caso, se espera que el primer argumento sea un número entero que representa el umbral para filtrar las ventas delftstack.com.

    La variable umbral se inicializa con el valor entero del primer argumento de la línea de comandos (sys.argv[1]).

    Se define un diccionario llamado ventas que contiene las ventas de cada mes del año.

    Se crea un nuevo diccionario llamado filtro, que contiene las entradas del diccionario ventas cuyos valores son mayores que el umbral.

    Finalmente, se imprime el diccionario filtro.

Para ejecutar este código desde la línea de comandos, debes proporcionar un argumento numérico, como se muestra en el siguiente ejemplo:

python script.py 20000

Donde script.py es el nombre del archivo que contiene el código proporcionado y 20000 es el umbral. El resultado sería un diccionario que contiene solo las ventas que superan el umbral de 20000.

Ten en cuenta que este código no es seguro en términos de manejo de errores y podría fallar si no se proporciona un argumento válido. Para mejorar este aspecto, podrías agregar un manejo de errores adecuado para garantizar que el argumento proporcionado sea un número entero válido antes de asignarlo a la variable umbral."""
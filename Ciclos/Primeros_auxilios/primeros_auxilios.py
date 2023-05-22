

#Se genera función para evaluar la respuesta

def evaluacion_respuesta(respuesta):
    respuesta = respuesta.lower()
    if respuesta == "si":
        return True
    elif respuesta == "no":
        return False
    else:
        while respuesta != "si" and respuesta != "no":
            respuesta = input("respuesta no válida, responder si o no, intente de nuevo: ")
            respuesta = respuesta.lower()
            if respuesta == "si":
                return True
            elif respuesta == "no":
                return False

def respira(evaluacion_respuesta):
    if evaluacion_respuesta == True:
        print("Rermitirle posición de suficiente ventilación")
    else:
        print("Administrar 5 ventilaciones y llamar a la ambulancia")
        
def signos(evaluacion_respuesta):
    if evaluacion_respuesta == True:
        print("Administrar compresiones torácicas hasta que llegue ambulancia")
    else:
        print("Reevaluar a la espera de la ambulancia")
        
def ambulancia(evaluacion_respuesta):
    return evaluacion_respuesta


print("""
Primeros Auxilios
=================
(Responder con si o no)""")
respuesta = input("¿Responde a los estimulos?\n>>> ")

def responde_estimulos(evaluacion_respuesta):
    if evaluacion_respuesta == True:
        print("Valorar la necesidad de llevarlo al hospital más cercano")
    else:
        print("Abrir la vía aérea")
        
responde_estimulos(evaluacion_respuesta(respuesta))

if evaluacion_respuesta(respuesta) == False:
    respuesta = input("¿Respira?\n>>> ")
    respira(evaluacion_respuesta(respuesta))

if evaluacion_respuesta(respuesta) == False:
    respuesta = input("¿Tiene signos de vida?\n>>> ")
    signos(evaluacion_respuesta(respuesta))
    

while ambulancia(evaluacion_respuesta(respuesta)) == False:
    respuesta = input("¿Llegó la ambulancia?\n>>> ")
    ambulancia(evaluacion_respuesta(respuesta))
    if ambulancia(evaluacion_respuesta(respuesta)) == True:
        print("Fin")
        break
    else:
        respuesta = input("¿Tiene signos de vida?\n>>> ")
        signos(evaluacion_respuesta(respuesta))
        
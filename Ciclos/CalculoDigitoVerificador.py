rut = input("Ingrese su Rut sin puntos ni dígito verificador:")
print()

rut = rut [::-1]
serie ="234567"*3

suma = 0
for i,j in zip(rut,serie):
    producto = int(i)*int(j)
    suma = suma + producto

modulo = suma % 11

dv = 11 - modulo

if dv == 10:
    dv = "K"
if dv == 11:
    dv = 0

print("Su dígito verificador es",dv) 
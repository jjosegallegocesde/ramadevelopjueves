#Funciones Lambda

# Funcion 1

# funcion tradicional
def clasificar(numero):
    if(numero % 2 == 0):
        return print("El numero es par")
    else:
        return print("El numero no es par")
        
clasificar(111)

#funcion lambda
clasificar2 = lambda numero: (numero % 2 == 0)

if(clasificar2(49)):
    print("El numero es par")
else:
    print("El numero no es par")
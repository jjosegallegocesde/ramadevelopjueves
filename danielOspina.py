#Función lambda que clasifique si un numero es par

def numeroPar(numero):
    if(numero%2==0):
        print(f"El número {numero} es par")
    else:
        print(f"El número {numero} NO es par")

numero=int(input("Ingrese un número: "))

numeroPar(numero)

#lambda


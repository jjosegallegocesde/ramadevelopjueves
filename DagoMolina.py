#("Funciones LambDa")

def saludar(nombre):
    return nombre
    
print(saludar("Dago Molina"))

#TRASFORMANDO EN LAMBDA FUNCTION
#Declarando funcion
saludar2 = lambda nombre : nombre
#Invocar funcion lambda
print(saludar2("Julian"))

#Retos
#1) Función lambda que clasifique si un numero es par
#Funcion Tradicional
def calcularNumeroPar(numero):
    if numero / 2:
        return 'El numero es par', numero
    else:
        return 'el numero es impar'
print(calcularNumeroPar(2))

#Funcion lambda
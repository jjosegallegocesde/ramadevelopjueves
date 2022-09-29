#("*FUNCIONES LAMBA*")

from pickle import FALSE


def saludar(nombre):
    return "Hola " + nombre

print(saludar("Johan"))

#LAMBDA

saludarL=lambda nombreL:"Hola " + nombreL

print(saludarL("Esteban"))

#Reto1

def compararNumeros(n):
    if n % 2 == 0:
        print("El número es par")
    else:
        print("El número es impar")
compararNumeros

#LAMBDA

compararNumerosL = lambda n:True if n % 2 == 0 else False
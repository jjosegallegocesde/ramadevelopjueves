""" #("Funciones Lamda")

#Declarar
from wsgiref.validate import InputWrapper


def saludar(nombre):
    return nombre

#Invocar o llamar una función
print(saludar("mateo"))

#Transformando en lambda function

#Declarando
saludar2=lambda nombre:nombre 
#invocar
print(saludar2("mateo"))
 """
#1.Función lambda que clasifique si es un numero es par
print("Digite un numero")
numero=int(input("Numero:"))

if(numero % 2 == 0 ):
    print("El numero es par")
else:
    print("El numero no es par")

#Funcion que sume 2 numeros 
from tkinter import Y


def sumarNumeros(numero1,numero2):
    return numero1+numero2

suma=sumarNumeros(5,2)
print('La suma es: ',suma)

#Funcion lambda que sume dos numeros 
numeroo1=int(input("Digite un numero: "))
numeroo2=int(input("Digite un numero: "))

sumar = lambda x,y : x + y

resultado = sumar(numeroo1, numeroo2)

print(f'La suma de los numeros es: {resultado}')
#Funcion lambda que mulriplique un numero por 100

def multiplicarCien(numero):
    numero * 100

resultado = multiplicarCien(5)

print(f'El resultado es: {resultado}')

#Funcion Lambda
n= int(input("Digite un número: "))

multiplicar = lambda x: x * 100

resultado = multiplicar(n)

print(f'La multiplicación de los números es {resultado}')
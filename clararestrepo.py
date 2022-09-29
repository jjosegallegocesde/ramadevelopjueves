#Declarar una función
def saludar(nombre):
    return  nombre

#Invocar / llamar una función
print(saludar("Clara"))

#Transformando en lambda function

#Declarando 
saludar2=lambda nombre:nombre
#Invocar / llamar una función
print(saludar2("Clara"))

#Funcion tradicional que defina si un numero es par o impar 

    
#Funcion lambda
x = int(input("Digite un número: "))
numerol = lambda num: num%2

if(numerol(x) !=0):
    print(f'El numero es impar {x}')
else:
    print(f'El numero es par {x}')
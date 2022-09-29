""" #("Funciones lambda")

#Declarar función
def saludar(nombre):
    return nombre


#Invocar función
print(saludar("Daniela"))


#Transformando en lambda function

#Declarando
saludar2 = lambda nombre: f'hola {nombre}'

#invocar 
print(saludar2("Daniela")) """


def obtenerPar(numero1):
    if(numero1 % 2 == 0):
        print(f"El numero {numero1} es par")
    else:
        print(f"El numero {numero1} es impar")


total = obtenerPar(208)

obtenerPar2 = lambda numero1: True if (numero1 % 2 == 0) else False


total = obtenerPar2(207)
print(total)


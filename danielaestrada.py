#("Funciones lambda")

#Declarar función
def saludar(nombre):
    return nombre


#Invocar función
print(saludar("Daniela"))


#Transformando en lambda function

#Declarando
saludar2 = lambda nombre: f'hola {nombre}'

#invocar 
print(saludar2("Daniela"))
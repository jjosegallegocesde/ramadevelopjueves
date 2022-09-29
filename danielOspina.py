#("FUNCIONES LAMBDA")

def saludar(nombre):
    return f'hola {nombre}'

print(saludar("Pedro"))

#transformando en lambda function

#declarando la función lambda
saludar2=lambda nombre: f'hola {nombre}' 

#invocando la función lambda

print(saludar2("Juan"))

#se usan para funciones de un propósito, en una sola línea
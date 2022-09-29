#Función que multiplique un número por 100
print("Digite un numero")
numero=int(input("Numero:"))

multiplicar= numero * 100

print(multiplicar)


#funcion lambda
numero=int(input("Numero:"))
multiplicar2=lambda numero:numero*100
multiplica=multiplicar2(5)
print(multiplica)
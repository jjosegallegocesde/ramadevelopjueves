from cmath import log
from pkgutil import read_code

def login():
    i = True
    contador = 0
    while(i):
        usuario = input("Digite el usuario: ")
        contraseña = input("DIgite la contraseña: ")
        if(usuario == "admin" and contraseña == "admin123"):
            print("Verdadero")
            i = False
        else:
            contador = contador + 1
        print(contador)
# login()


def rectangulo():
    anchoo = int(input("Digite el ancho del rectangulo"))
    largo = int(input("Digite el largo del rectangulo"))
    area = anchoo * largo
    perimetro = (anchoo * 2)+(largo * 2)
    while largo > 0 :
        ancho = anchoo
        while ancho > 0 :
            print("*"*ancho)
            ancho = 0
        largo = largo - 1
    print(f'Area: {area}') 
    print(f'Perimetro: {perimetro}') 

rectangulo()










# Funcion 1

# funcion tradicional
def clasificar(numero):
    if(numero % 2 == 0):
        return print("El numero es par")
    else:
        return print("El numero no es par")
        
clasificar(111)

#funcion lambda
clasificar2 = lambda numero: (numero % 2 == 0)

if(clasificar2(49)):
    print("El numero es par")
else:
    print("El numero no es par")
    
    
    
    
    
    
    
    from audioop import mul


print("holaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
print("ganaron el parciaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaal")

def multiplicar(numero):
    return print(numero*100)

multiplicar(50)

multiplicar2 = lambda numero : print(numero*100)

multiplicar2(100)
        
        
        
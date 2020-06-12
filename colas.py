cola=[]

def agregar(numero):
    cola.append(numero)

def remover(b):
    if b<10:
        for i in range (b):
            cola.pop(0)
    elif b>10:
        print("Su pila solo tiene 10 digitos")
        eliminarcola()

def eliminarcola():
    b=int(input("Diga cuantas letras quiere eliminar de la cola"))
    remover(b)
    print("Su cola es", cola)

def agrenumero():
    for i in range (10):
        numero = input("Dígame un nombre ")
        agregar(numero)

    print("Su cola es", cola)
    eliminarcola()

agrenumero()
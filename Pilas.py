pila=[]

def agregar(numero):
    pila.append(numero)

def remover(b):
    if b<10:
        for i in range (b):
            pila.pop()
    elif b>10:
        print("Su pila solo tiene 10 digitos")
        eliminarpila()

def eliminarpila():
    b=int(input("Diga cuantos numeros quiere eliminar de la pila"))
    remover(b)

    print("Su pila es", pila)

        
def agrenumero():
    for i in range (10):
        numero = int(input("Dígame un número: "))
        agregar(numero)
    
    print("Su pila es", pila)
    eliminarpila()
    

agrenumero()





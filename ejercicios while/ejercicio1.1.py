def contadorascendente (num):
    cadena= " "
    cont=0
    while cont <= num:
        cadena += str(cont)+"\n"
        cont+=1
    return cadena
num=int(input("Ingresa un numero "))
print(contadorascendente(num))

def sumanumeros(num):
    suma=0
    cont=0
    while cont <= num:
        suma += cont
        cont += 1 
    print(suma)
num=int(input("Ingresa un numero "))
contadorascendente(num)

def factoriar (num):
    fact=1
    cont=0
    while fact <= num:
        fact *= cont
        cont += 1
    print(fact)
num=int(input("Ingresa un numero "))
factoriar(num)
lista= []
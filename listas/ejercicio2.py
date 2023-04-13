print("Curso de Fundamentos de Python.")
print("Nombre:Nayeli Gallegos")
print("Fecha: 10/04/2023")

#CURSO DE FUNDAMENTOS DE PYTHON 
#EJERCICIOS DE LISTAS A RESOLVER
#Crea una lista vacía llamada numeros e introduce los números del 1 al 5. Luego, muestra la lista por pantalla.
numeros=[]

for e in range(1,6):
    numeros.append(e)
print("la lista ",numeros )
#Crea una lista con los nombres de tus amigos y muestra por pantalla el primer elemento de la lista.
nombres=["mela","evelin","jenny","danny","alex"]
print("el primer elemento : ", nombres[0])
#Crea una lista con los números del 1 al 10 y muestra por pantalla los números pares.
numeros2=[1,2,3,4,5,6,7,8,9,10 ]
for e in numeros2:
    if e % 2 == 0: 
        print("Los numeros pares ", e  )

#Crea una lista con los nombres de tus amigos y muestra por pantalla el último elemento de la lista.
nombres=["mela","evelin","jenny","danny","alex"]
print("el ultimo elemento de la lista  : ", nombres[-1])

#Crea una lista con los números del 1 al 10 y muestra por pantalla el último elemento de la lista.
numeros=[1,2,3,4,5,6,7,8,9,10 ]
print("El ultimo elemento de la lista de numeros: ",numeros[-1])

#Crea una lista con los números del 1 al 10 y muestra por pantalla los números impares.
numeros=[1,2,3,4,5,6,7,8,9,10 ]
for e in numeros :
    if e % 2 == 1:
        print("Numeros impares: ", e)

#Crea una lista con los nombres de tus amigos y añade un nuevo amigo a la lista. Luego, muestra la lista por pantalla.
nombres.insert(2,"darwin ")
print(" Agregado un nuevo elemento : ",nombres)

#Crea una lista con los números del 1 al 10 y muestra por pantalla el primer y el último elemento de la lista.
numeros3=[1,2,3,4,5,6,7,8,9,10 ]
print("El primer elemento",numeros3[0], "y","El utlmimo elemento de la lista ", numeros3[-1])
#Crea una lista con los nombres de tus amigos y muestra por pantalla el número de elementos de la lista.
nombres=["mela","evelin","jenny","danny","alex"]
print("Numero de elementos ", len(nombres))

#Crea una lista con los números del 1 al 10 y muestra por pantalla la suma de todos los elementos de la lista.

numeros=[1,2,3,4,5,6,7,8,9,10]
suma = 0

for e in numeros:
    suma= suma + e 
print("la suma total ", suma)
print("la suma total ",sum(numeros))




    
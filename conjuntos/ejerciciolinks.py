#CURSO DE FUNDAMENTOS DE PYTHON 
#EJERCICIOS DE CONJUNTOS
#Crear un conjunto con los números del 1 al 10 e imprimirlo en pantalla.
a=set()
a.add(1)
a.add(2)
a.add(3)
a.add(4)
a.add(5)
a.add(6)
a.add(7)
a.add(8)
a.add(9)
a.add(10)
print("La lista del 1 al 10 : ", a)
#Crear dos conjuntos, uno con los números pares del 1 al 10 y otro con los impares del 1 al 10. Luego, imprimir los conjuntos y la intersección entre ello
pares= set(num for num in range (2,11,2))
impares= set(num for num in range(1,11,2))
print("Conjunto de pares",pares)
print("Conjunto de impares ", impares)
print("Interseccion de conjuntos: ",pares.intersection(impares))
#Crear un conjunto con los elementos "manzana", "banana" y "naranja". Luego, pedirle al usuario que ingrese un elemento y determinar si ese elemento se encuentra en el conjunto o no.
frutas={"manzana", "banana","naranja"}
elemento= input("Ingrese un elemento: ")
if elemento in frutas:
    print(elemento, " se encuentra en la lista de frutas ")
else:
    print(elemento,"no se encuentra en la lista de frutas ")
#Crear un conjunto con los números del 1 al 5 y otro con los números del 4 al 8. Luego, unir los conjuntos y eliminar los elementos repetidos. Finalmente, imprimir el conjunto resultante.
a={1,2,3,4,5}
b={4,5,6,7,8}
print("Union de los conjuntos: ", a.union(b))

#Crear un conjunto con los elementos "leche", "pan", "huevos" y "azúcar". Luego, eliminar el elemento "azúcar" del conjunto y agregar el elemento "harina". Finalmente, imprimir el conjunto resultante.
elementos={"leche", "pan", "huevos" ,"azúcar"}
elementos.discard("azúcar")
elementos.add("harina")
print("Conjunto resultante: ",elementos)
#Crear un conjunto con los nombres "Juan", "María", "Pedro" y "Luisa". Luego, imprimir el número de elementos del conjunto.
nombres={"Juan", "María", "Pedro" ,"Luisa"}
print("Numero de elementos del conjunto: ",len(nombres))
#Crear dos conjuntos, uno con los números del 1 al 5 y otro con los números del 4 al 8. Luego, imprimir los conjuntos y la diferencia simétrica entre ellos.
cant1={1,2,3,4,5}
cant2={4,5,6,7,8}
diferencia= cant1.symmetric_difference(cant2)
print("Diferencia simetrica: ",diferencia)
#Crear un conjunto con los números del 1 al 10 y otro con los números del 5 al 15. Luego, imprimir los conjuntos y la unión entre ellos.
a=set(range(1,11))
b=set(range(5,16))
print("Conjunto 1: ",a)
print("Conjunto 2: ",b)
c=a.union(b)
print("Union de conjuntos: ",c)
#Crear un conjunto con los elementos "manzana", "banana", "naranja" y "pera". Luego, imprimir los elementos del conjunto en orden alfabético.
elementos={"manzana", "banana", "naranja" , "pera"}
print("Elementos del conjunto en orden alfabetico: ",sorted(elementos))
#Crear un conjunto con los números del 1 al 10 y otro con los números del 6 al 15. Luego, imprimir los conjuntos y la intersección entre ellos.
conj1=set(range(1,11))
conj2=set(range(6,16))
print("Conjunto 1",conj1)
print("Conjunto 2",conj2)
print("Interseccion de conjuntos",conj1.intersection(conj2))
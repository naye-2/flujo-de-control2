print("Curso de Fundamentos de Python.")
print("Nombre:Nayeli Gallegos")
print("Fecha: 10/04/2023")
print("Relizar ejercicios sbre listas ")
#1. Crear una lista de numeros del 1 al 5
#2. Accede al elemto 3 de la lista:
listas=[1,2,10,3,9,5]
print("acceda al  elemento ",listas[3])
#3. Modifica un elemento de la lista:
listas[2]=12
print("Modificado :", listas)
#4. Agrega el elemento 9 al final de la lista
listas.append(9)
print("Agregar elementos ", listas)
#5. Eliminar el elemento 2 de la lista:
listas.remove(2)
print("Eliminado un elemento", listas)
#7. Ordenar una lista:
print("Lista ordenada ", sorted(listas))

#6. Recorrer una lista con un bucle for:
for e in listas:
    print("listas recorridad  " , e)
#8. Obtener la longitud de una lista:
len (listas)
print("Longitud de la lista ", listas )
#9. Comprobar si un elemento está en la lista:
if 5 in listas:
    print("el numero esta en lista"  )
else:
    print("no esta en la lista ")

#10. presentar el numero minimo
print("Minimo de la lista",min(listas))
#11. Presentar el numero maximo
print("Maximo de la lista ", max(listas))



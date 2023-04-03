print("Curso de Fundamentos de Python.")
print("Nombre:Nayeli Gallegos")
print("Fecha: 01/03/2023")

"""###7.
 Escribir un programa que pida al usuario una nota del 0 al 10 y muestre por pantalla la calificación según la siguiente tabla:
- 0-2: Muy deficiente
- 3-4: Insuficiente
- 5-6: Suficiente
- 7: Bien
- 8-9: Notable
- 10: Sobresaliente"""

calificacion=int(input("Ingresar su calificacion: "))

if calificacion >= 0 and calificacion <=2:
    print("Su calificacion de " , calificacion,"es Muy deficiente")
elif calificacion >= 3 and calificacion <= 4 :
    print("Su calificacion de ", calificacion, " es Insuficiente ")
elif calificacion >= 5 and calificacion <= 6:
    print("Su calificacion de " , calificacion, "es Suficiente ")
elif calificacion ==7  :
    print("Su calificacion de " , calificacion," esta bien ")
elif calificacion >= 8 and calificacion <= 9:
    print("Su califcacion", calificacion," es Notable ")
elif calificacion == 10 :
    print("Su calificacion de " , calificacion, " es Sobresaliente ")
else:
    print("El valor ingresdao no esta dentro del rango de calificaciones ")
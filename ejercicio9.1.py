print("Curso de Fundamentos de Python.")
print("Nombre:Nayeli Gallegos")
print("Fecha: 31/03/2023")

print("Detalles: Calificaciones finales.")

calificacion=float(input("Ingresa tu nota final:"))

if calificacion >=9.50 and calificacion <=10:
    print("Su calificacion es Excelente")
elif calificacion >=8.50 and calificacion < 9.50:
    print("Su calificacion es Muy Buena")
elif calificacion >= 7.00 and calificacion < 8.50:
    print("Su calificacion es Buena.")
elif calificacion >=4.00 and calificacion < 7.00:
    print("Su calificacion es Regular")
elif calificacion >=0.00 and calificacion < 4.00:
    print("Su califciacion es Deficiente")
else:
    print(" El valor ingresado no esta dentro del rango de calificaciones  ")
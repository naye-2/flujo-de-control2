print("Curso de Fundamentos de Python.")
print("Nombre:Nayeli Gallegos")
print("Fecha: 31/03/2023")

print("Detalles: calificacion de un examen ")
calificacion= int (input( "ingrese la calificacion del examen "))

if calificacion>=90:
    print(" La calificacion es A")
elif calificacion>=80:
    print(" La calificacion es B")
elif calificacion>=70:
    print(" la calificacion es C")
elif calificacion>=60:
    print("La calificacion es D")
else :
    print("Su calificacion es F")
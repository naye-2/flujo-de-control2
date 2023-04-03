print("Curso de Fundamentos de Python.")
print("Nombre:Nayeli Gallegos")
print("Fecha: 01/04/2023")

#Programa para imprimir el día de la semana correspondiente a un número del 1 al 7:

semana=int(input("Ingrese un numero para saber el dia de la semana: "))

if semana == 1 :
    print("el numero",semana, "corresponde al lunes")
elif semana ==2:
    print("el numero ",semana, " corresponde al martes")
elif semana ==3:
    print("el numero ",semana, " corresponde al miercoles ")
elif semana == 4:
    print("el numero ",semana, " corresponde al jueves ")
elif semana == 5:
    print("el numero ",semana, "corresponde al viernes ")
elif semana == 6: 
    print("el numero ",semana, "corresponde al sabado ")
elif semana == 7 :
    print("el numero ",semana, "corresponde al domingo ")
else:
    print("El numero ingresado no corresponde a ningun dia de la semana ")
print("Curso de Fundamentos de Python.")
print("Nombre:Nayeli Gallegos")
print("Fecha: 31/03/2023")

valor_1=int(input(" Ingresa valor 1  "))
valor_2=int(input(" Ingresa valor 2  "))

print("Presione 1 para sumar")
print("Presione 2 para restar")
print("Presione 3 para multiplicar")
opcion=int(input("Que opcion desea "))

if opcion==1:
    print("La suma de los valores es", valor_1+valor_2)
elif opcion==2:
    print("La resta de los valores es", valor_1-valor_2 )
elif opcion==3:
    print("La multiplicación es",valor_1*valor_2)
else:
    print("No es correcta la opcion")
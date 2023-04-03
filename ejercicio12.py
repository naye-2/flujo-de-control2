print("Curso de Fundamentos de Python.")
print("Nombre:Nayeli Gallegos")
print("Fecha: 1/04/2023")

#Determine si un numero es negativo,positivo o cero

numero=int(input("Ingrese un numero "))

if numero > 0:
    print("El numero",numero, "es positivo ")
elif numero < 0:
    print ("El numero ", numero, "es negativo")
else:
    print("El numero",numero, "es cero ")
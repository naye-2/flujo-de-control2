print("Curso de Fundamentos de Python.")
print("Nombre:Nayeli Gallegos")
print("Fecha: 31/03/2023")

numero=input("Ingrese un numero: ")

if len(numero) != 1:
    print ("No se puede procesar el dato,debe ingresar un numero")

elif numero in "123456789":
    print("El numero", numero ," se encuentra dentro del rango")
else:
    print("El numero ingresado no se encuentra dentro del rango")
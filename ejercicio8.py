print("Curso de Fundamentos de Python.")
print("Nombre:Nayeli Gallegos")
print("Fecha: 31/03/2023")

letra = input("Ingrese una letra: ")

if len(letra) != 1:
    print("No se puede procesar el dato. Debe ingresar una sola letra.")
elif letra in "aeiouAEIOU":
    print("Es vocal")
else:
    print("No es vocal")
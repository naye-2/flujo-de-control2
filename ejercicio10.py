print("Curso de Fundamentos de Python.")
print("Nombre:Nayeli Gallegos")
print("Fecha: 01/04/2023")

año=int(input("Ingresa el año : "))
if año % 4 ==0 and año % 100 != 0 :
    print ("El año " , año, "es bisiesto ")
elif año % 400 ==0:
    print("El ", año, "es divisible entre 400 ")
else:
    print("los numeros ingresado no es bisiesto y por lo tanto no es divible entre los numeros propuestos ")
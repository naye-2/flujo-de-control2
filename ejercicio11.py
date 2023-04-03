print("Curso de Fundamentos de Python.")
print("Nombre:Nayeli Gallegos")
print("Fecha: 1/04/2023")

# Determinar el mayor de tres numeros.

a=int(input("Ingresar el primer numero: "))
b=int(input("Ingresar el segundo numero: "))
c=int(input("Ingresar el tercer numero: "))

if a>b and a>c :
    print("El numero ",a, "es mayor.")
elif b>a and b>c : 
    print("El numero", b, " es mayor ")  
elif c>a and c>b:
    print("El numero",c, "es mayor")
else:
    print("Ninguno es mayor ") 
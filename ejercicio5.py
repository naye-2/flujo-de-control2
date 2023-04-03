print("Curso de Fundamentos de Python.")
print("Nombre:Nayeli Gallegos")
print("Fecha: 30/03/2023")

impuesto=0
salario=float(input("Ingrese su sueldo "))

if salario<10000:
    print("Impuestos es al 5%")
    impuesto=5/100
elif salario >= 100000 and salario <= 20000:
    print("Se paga un impuetso de 15%")
    impuesto=15/100
elif salario >= 20000 and salario<=35000:
    print("Se paga un impuesto de 20%")
    impuesto=20/100
elif salario >=35000 and salario< 60000:
    print("Se paga un impuesto del 30%")
    impuesto=30/100
elif salario >= 60000:
    print("Paga un impuesto del 45%")
    impuesto=45/100
else:
    print("el salrio ingresado no es correcto")

total= salario* impuesto
print ("el valor del impuesto a pagar es: ",total )
print("El salario a resibir es:",salario-total)
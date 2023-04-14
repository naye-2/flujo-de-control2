###CURSO DE FUNDAMENTOS DE PYTHON
#Trabajar los ejercicios con funciones, para llamarlos deberá de crear un menu en el que le permitira seleccionar al usuario que ejercicios ejecutar.

from metodos import *


opcion=0
while opcion >=0 and opcion <=0:
    
    print("1.Contador ascendente ") 
    print("2. Contasdor ascendente ")
    print("3.Suma de numeros ")
    print("4.Factorial ")
    print("5.Adivinar un  numero")
    print("6.Contador de vocales ")
    print("7.Suma de numeros pares ")
    print("8.Calculo de potencia ")
    print("9.Calculo de promedio ")
    print("10.Contador de palabras ")
    print("0. Salir")
    opcion= int(input("Ingrese una opcion: "))
    if opcion == 0:
        print("Ha selecionado salir ")
        break
    elif opcion == 1:
        print("Ha selecionado la opcion 1 ")
        num=int(input("Ingresa un numero "))
        print("Contador ascendente")
        contadorascendente(num)
    elif opcion==2:
        print("Ha seleccionado la opcion 2")
        num=int(input("Ingresa un numero "))
        print("Contador descendente")
        contadordescendente (num)
    elif opcion==3:
        print("Ha seleccionado la opcion 3")
        num=int(input("Ingresa un numero "))
        sumanumeros(num)
    elif opcion==4:
        print("Ha seleccionado la opcion 4 ")
        numero=int(input("Ingrese un numero: "))
        print(factoriar(numero))
        
    elif opcion==5:
        print("Ha seleccionado la opcion 5 ")
        aleatorio=random.randint(1,10)
        print("El numero que se genera es :" , str(aleatorio))
        adivinar(aleatorio)
    elif opcion==6:
        print("Ha seleccionado la opcion 6")
        vocales=input("Ingresa una cadena de texto ")
        print(contador(vocales))
    elif opcion==7:
        print("Ha seleccionado la opcion 7")
        numeros= int(input("Ingese un numero: "))
        print("La suma de los numeros pares desde cero hasta ",numeros,"es",suma(numeros))
    elif opcion==8:
        print("Ha seleccionado la opcion 8")
        num=int(input("Ingresa un valor: "))
        exponente=int(input("Ingresar el exponente: "))
        potencia(num,exponente)
    elif opcion==9:
        print("Ha selecionado la opcion 9 ")
        num=input("Ingresar una lista separado por comas ")
        num_list=[int(num)for num in num.split(",")]
        print(promedio(num_list))
    elif opcion== 10:
        print("Ha seleccionado la opcion 10 ")
        palabras = input("Ingrese una frase: ")
        print(contador_palabras(palabras))
    else:
        print("La opcion ingresado no esta dentro del menu  ")
        
        
        
        
        
    
         
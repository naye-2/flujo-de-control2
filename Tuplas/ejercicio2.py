#CURSO DE FUNDAMENTOS DE PYTHON 
#EJERCICIOS DE TUPLAS
#Crear una tupla de números enteros y calcular su suma y promedio.
numeros=(2,3,4,5,6,7,8,9)
suma=0
for e in numeros:
    suma += e
promedio=suma/len(numeros)
print("la suma es " , suma)
print("su promedio seria " , promedio)
#Crear dos tuplas de la misma longitud y crear una nueva tupla que contenga la suma de los elementos correspondientes de ambas tuplas.
tupl1=(1,2,3,4,5)
tupl2=(1,2,3,4,5)
suma_tuplas = tuple(map(sum, zip(tupl1, tupl2)))
print("La suma de los elementos ",suma_tuplas)
#Crear una tupla de nombres y ordenarla alfabéticamente.
tupla=("naye","miri","eve","jenny")
tupla2=sorted(tupla)
print("Ordenado alfabeticamnete ",tupla2)
#Crear una tupla de números y encontrar el valor mínimo y máximo.
numeros3=[2,3,4,5,6,7,8,9,45,2,4]
minimo=min(numeros3)
maximo=max(numeros3)
print("Valor maximo: ",maximo)
print("Valor minimo: ",minimo)
#Crear una tupla de números y convertirla en una lista.
tupla=(1,2,3,4,5,67,8,9)
print("Convertida en lista : ",list(tupla))
#Crear una tupla con los días de la semana y mostrar el tercer elemento.
semana=("lunes","martes","miercoles","jueves","viernes")
print("el tercer elemento", semana[2])
#Crear una tupla con números enteros y mostrar aquellos que son pares.
numeros=(1,2,3,4,5)
for e in numeros:
    if e % 2 == 0: 
       print("numeros pares: ", e)
#Crear una tupla con los meses del año y mostrar aquellos que tienen más de cinco letras.
meses=("enero","febrero","marzo","abril","mayo","junio","julio")
for mes in meses:
    if len(mes) > 5:
       print("tiene mas de 5 letras \n",mes)
#Crear una tupla con las edades de varias personas y mostrar la cantidad de personas mayores de 18 años.
numeros=(15,34,56,7,8,98,45,23)
for e in numeros:
    if e > 18 :
        print("mayores de edad ", e)
#Crear una tupla de tuplas que contienen información de libros y mostrar el título del tercer libro.
libros=(("flor salvador","boulevard", ),
        ("Johana marcus", "Antes de diciembre"),
        ("Johana marcus","Despues de diciembre"))
posicion=libros.index(("Johana marcus","Despues de diciembre"))
print(posicion)
print("Titulo del tercer libro : ", libros[posicion][1])



print("Curso de Fundamentos de Python.")
print("Nombre:Nayeli Gallegos")
print("Fecha: 10/04/2023")
#EJERCICIOS DE TUPLAS
#Crear una tupla vacía:
tupla=()
print(tupla)
#Crear una tupla con algunos elementos:
tupla=([2,3,4,],"hola",50,(20,"tupla"))
print("Elementos ",tupla)
#Acceder a un elemento de la tupla:
print("Acceder a un elemento ",tupla[2])
#Intentar modificar un elemento de la tupla (esto producirá un error ya que las tuplas son inmutables):
"no es posible"
#Concatenar dos tuplas:
cant1=(1,2,3,4)
cant2=(5,6,7,8,9)
cant3=cant1+cant2
print("Concatenar dos tuplas ",cant3)
#Obtener la longitud de una tupla:
numeros2=(2,3,4,5,6,7)
print("Longitud de la tupla ",len(numeros2))
#Convertir una tupla en una lista:
tupla1=(1,2,3,4,5,6,7,8,9,10)
print("Convertido en lista ",list(tupla1))
#Convertir una lista en una tupla:
numeros3=[2,3,4,5,6,7]
print("Convertido en tupla",tuple(numeros3))
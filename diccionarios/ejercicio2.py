#CURSO DE FUNDAMENTOS DE PYTHON 
#EJERCICIOS DE DICCIONARIOS
#1.Crea un diccionario vacío y agrega tres elementos de la siguiente forma: "clave": valor
alumnos={}

#2.Dado el siguiente diccionario:
personas = {"Juan": 28, "María": 20, "Pedro": 32, "Ana": 25}
#a) Imprime la edad de Juan.
print("La edad de Juan: ",personas.get("Juan"))

#b) Agrega un nuevo elemento al diccionario con la clave "Luis" y la edad 18.
personas["luis"]="18"
print("Agrega un nuevo elemento: ",personas)

#c) Elimina el elemento con la clave "Pedro".
personas.pop("Pedro")
print("Elimado un elemento ",personas)
#3.Dado el siguiente diccionario:
ventas = {"manzanas": 10, "naranjas": 5, "peras": 8}
#a) Imprime la cantidad de manzanas vendidas.
print("la cantidad de manzanas vendidas es",ventas["manzanas"])
#b) Agrega 3 elementos más al diccionario: "limones": 12, "sandías": 3, "melones": 5.
ventas["limones"],ventas["sandias"],ventas["melones"]="12","3","5"
print("Elementos agregados : ",ventas)
#c) Imprime las claves del diccionario.
print("Claves del diccionario: ",ventas.keys())
#4. Dado el siguiente diccionario:
alumnos = {"Juan": {"edad": 22, "promedio": 8.5}, "María": {"edad": 20, "promedio": 9.0}, "Pedro": {"edad": 25, "promedio": 7.5}}
#a) Imprime la edad de Juan.
print("La edad de Juan ",alumnos["Juan"]["edad"])
#b) Imprime el promedio de María.
print("El promedio de Maria ",alumnos["María"]["promedio"])
#c) Agrega un nuevo elemento al diccionario con la clave "Ana" y los valores "edad": 19 y "promedio": 8.0.
alumnos["Ana"]={"edad":19,"promedio":8.0}
print("Elementos agregados", alumnos)
alumnos.items()
for c,v in alumnos.items():
    if v["edad"]>= 20 and  v["edad"]<= 22:
        print(c)
#5. Dado el siguiente diccionario:
empleados = {"Juan": {"departamento": "Ventas", "sueldo": 1500}, "María": {"departamento": "Contabilidad", "sueldo": 1800}, "Pedro": {"departamento": "Ventas", "sueldo": 1700}, "Ana": {"departamento": "Recursos Humanos", "sueldo": 1900}}
#a) Imprime el sueldo de Pedro.
print("El sueldo de Pedro",empleados["Pedro"]["sueldo"])
#b) Cambia el sueldo de Ana a 2000.
empleados["Ana"]["sueldo"]=2000
print(empleados)
#c) Crea un nuevo diccionario con los empleados del departamento de Ventas.
empleados2={"Juan": {"departamento": "Ventas", "sueldo": 1500},"Pedro": {"departamento": "Ventas","sueldo":1700}}
print("Empleados del departamento de ventas ",empleados2)
#6.Dado el siguiente diccionario:
cursos = {
    "Pedro": ["Matemáticas", "Biología", "Historia"],
    "María": ["Física", "Química", "Literatura"]
}
#a) Imprime las materias en las que está inscrito Pedro.
print("Materias de Pedro",cursos["Pedro"])
#b) Agrega una materia más a la lista de materias de María: "Programación".
cursos ["María"].append("Programacion")
print("Agregado un nuevo elemento ",cursos)
#c) Crea un nuevo diccionario con los estudiantes que están inscritos en la materia de Biología.

biologia = {}

for estudiante, cursos in cursos.items():
    if "Biología" in cursos:
        biologia[estudiante] = cursos

print(biologia)
#7. Dado el siguiente diccionario:
productos = {'manzanas': 2.99, 'naranjas': 1.99, 'peras': 3.99, 'uvas': 4.99, 'kiwis': 0.99, 'duraznos': 2.49}
stock = {'manzanas': 100, 'naranjas': 50, 'peras': 25, 'uvas': 75, 'kiwis': 200, 'duraznos': 60}
#a) Imprime el precio de las naranjas.
print("Precio de las naranjas",productos["manzanas"])
#b) Cambia el stock de peras a 12.
stock ["peras"]= 12
print(stock)
#c) Crea una función que calcule el valor total de los productos en el diccionario.
def calcularvalor (productos,stock):
    valortotal=0
    for productos,precio in productos.items():
        if productos in stock:
            cantidad= stock[productos]
            valortotal += precio* cantidad
    return valortotal
valortotal = calcularvalor(productos, stock)
print(valortotal)
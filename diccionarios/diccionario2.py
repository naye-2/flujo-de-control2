instituto= {"carreras":["big data","desarrollo de software","entrenameinto deportivo", "cyberseguridad", "tributacion"],
            "materias": ["calculo ", "estadistica","programacion","introduccion a big data", "matematica discreta","Lenguaje "],
            "profesores" : ["Vilma","Paul","Lady","Fabian ","Juliana","Veronica"],
            "notas": ["79","83","80","90", "73","94"]}
print(instituto)
print("Careras del instituto",instituto["carreras"])
print("Materias del instituto",instituto["materias"])
print("Profesores del instituto",instituto["profesores"])
print("Notas obtenidas",instituto["notas"])

suma=0

for e in instituto["notas"]:
    suma += float(e )
print(suma/len(instituto["notas"]))
print(round(suma/len(instituto["notas"]),2))

minimo=min(instituto["notas"])
print(minimo)
posicion=instituto["notas"].index(minimo)
print(instituto["profesores"][posicion])
print(instituto["materias"][posicion])
print("la nota minima es ",min(instituto["notas"]) ,"su profesor  es ",instituto["profesores"][posicion],"su materia es",instituto["materias"][posicion])

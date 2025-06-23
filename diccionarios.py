mi_diccionario = dict()
otro_diccionario = {}

print(type(mi_diccionario))
print(type(otro_diccionario))

otro_diccionario = {"Nombre":"Antony","Apellido":"Toribio","Edad": 22, 1: "Python"}

mi_diccionario = {
  "Nombre":"Antony",
  "Apellido":"Toribio",
  "Edad": 22, 
  "Lenguajes": {
    "Java",
    "TypeScript",
    "SQL"
  }

}

print(otro_diccionario)
print(mi_diccionario)
print(mi_diccionario["Lenguajes"])

otro_diccionario["Apellido"] = "Pérez"
print(otro_diccionario["Apellido"])
print(otro_diccionario[1])

mi_diccionario["Calle"] = "Kaminal"
print(mi_diccionario)

del mi_diccionario["Calle"]
print(mi_diccionario)

print("Antony" in mi_diccionario)
print("Calle" in mi_diccionario)

print(mi_diccionario.keys())
print(mi_diccionario.items())
print(mi_diccionario.values())

nuevo_diccionario = dict.fromkeys((mi_diccionario))
print(nuevo_diccionario)
nuevo_diccionario = dict.fromkeys(("Nombre", 1, "Piso"))
print(nuevo_diccionario)
nuevo_diccionario = dict.fromkeys((mi_diccionario))
print(nuevo_diccionario)
nuevo_diccionario = dict.fromkeys(mi_diccionario, ("Antony", "Mesa"))
print(nuevo_diccionario)
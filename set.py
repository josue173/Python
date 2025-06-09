mi_set = set()
mi_otro_set = {}

print(type(mi_set))
print(type(mi_otro_set)) # Al inicio, un set es un diccionario

mi_otro_set = {'Antony', 17, 0.21, True}
print(type(mi_otro_set)) 

print(len(mi_otro_set))

mi_otro_set.add("Hola")
print(mi_otro_set) # Un set no es una estructura ordenada
mi_otro_set.add("Hola") # Un set no admite datos repetidos
print(mi_otro_set)

print("Hola" in mi_otro_set)
print("Hol" in mi_otro_set)

mi_otro_set.remove("Antony")
print(mi_otro_set)

mi_otro_set.clear()
print(len(mi_otro_set))

del mi_otro_set
# print(mi_otro_set)

mi_set = {"Antony", "hola", 2}
mi_lista = list(mi_set)
print(mi_lista)

mis_lenguajes = {"Python", "TypeScript", "Java", "SQL"}

mi_nuevo_set = mi_set.union(mis_lenguajes)
print(mi_nuevo_set)

mi_nuevo_set = mi_set.union(mis_lenguajes)
print(mi_nuevo_set.difference(mis_lenguajes))

# Si se queire que la información sea inmutable y el orden es importante, se usan tuplas
# Las listas si son modificables
# Si el orden es irrelevante y no se quieren repetir datos, se usan sets
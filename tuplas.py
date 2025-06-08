tupla = tuple()
otra_tupla = ()

tupla = (42,534.523, "Antony", "Toribio")
mi_otra_tupla = (35,35,36)

print(tupla)
print(type(tupla))
print(tupla[0])

print(tupla.count("Antony"))
print(tupla.index("Antony"))

#tupla[1] = 1.8
sumar_tuplas = tupla + mi_otra_tupla
print(sumar_tuplas)

print(sumar_tuplas[3:4]) # Omitir 3 datos e imprimir hasta la 4 

lista = list(tupla)
print(type(lista))
lista[3] = "Holi"
lista.insert(1, "Azul")
print(tuple(lista))

del lista 
print(lista)
mi_lista = list()

otra_lista = []

print(len(mi_lista))

mi_lista = [32,48,120,84,84,2,5,9,7,5,47,1,2,4]

print(mi_lista)
print(len(mi_lista))

otra_lista = [32, 42.534, "Antony", "Toribio"]

print(type(otra_lista))
print(type(mi_lista))
print(otra_lista[0])
y = otra_lista.count(42.534)
print(y)

edad, salario, nombre, apellido = otra_lista
print(salario)

otra_lista.append("HOLA HOLA")
print(otra_lista)

otra_lista.insert(1, "Azul")
print(otra_lista)

otra_lista.remove("Antony") # Elimina un elemento que se sabe que existe
print(otra_lista)

otra_lista.pop() # Retorna el elemento que se elimina
print(otra_lista)

otra_lista.pop(1) # Elimina el elemento que se encuentra en el índice y hace retorno
print(otra_lista)

print(mi_lista)
del mi_lista[1] # Elimina un elemento sin hacer retorno
print(mi_lista)

#mi_lista.clear() # Elimina todos los elementos
#print(mi_lista)

nueva_lista = mi_lista.copy()
print("Lista original: ", mi_lista)
print("Nueva lista: ", nueva_lista)
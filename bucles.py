
mi_condicion = 0

while mi_condicion < 10:
  print("Entra")
  print(mi_condicion)
  mi_condicion += 1
else:
  print("Mi condición es mayor o igual que 10")

while mi_condicion < 20:
    mi_condicion += 1
    if mi_condicion == 15:
      print('Se detiene la ejecución')
      break
    print('El número es %d' %(mi_condicion))
      

print('La ejecución continúa')

# FOR

mi_lista = [12,23,34,45,56,67,78,89]

for element in mi_lista:
  print('El número es: %s' %(element))

mi_set = {12,23,45}

for element in mi_set:
  print(element)

mi_diccionario = {"Nombre":"Antony","Apellido":"Toribio","Edad": 22, 1: "Python"}

for element in mi_diccionario:
  print(element)

for element in list(mi_diccionario.values()):
  print(element)
  if type(element) == int:
    print("Es la edad")
    break
else:
  print('El bucle para el diccionar ha terminado.')
mi_condicion = True

if mi_condicion:
  print("Primera condicional")

print("Me salí del if")

mi_condicion = 5*3

if mi_condicion == 10:
  print("Es 10")
elif mi_condicion > 10 and mi_condicion < 20:
  print("Es menor o igual que 10 y menor a 20")
elif mi_condicion == 25:
  print("Es 5")
else:
  print("Es menor o igual que 10 o mayor o igual que 20")

print("Continua 2")

mi_string = ""

if not mi_string:
  print("La cadena está vacía")

if mi_string:
  print("Hay información")

if mi_string == "TEXTO":
  print("Coincidencia")
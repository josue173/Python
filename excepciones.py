# print(5+5)

numeroUno = 1
numeroDos = 31

numeroDos = "1"

# print(numeroUno + numeroDos)

# Solo try

# try:
#   print(numeroUno + numeroDos)
#   print('Sin error')
# except:
#   print('Se ha producido un error')

# try mamadisimo

# try:
#   print(numeroUno + numeroDos)
#   print('Sin error')
# except:
#   print('Se ha producido un error')
# else:
#   print('La ejecuciòn continúa correctamente')

# try super mamadísimo

try:
  print(numeroUno + numeroDos)
  print('Sin error')
except:
  print('Se ha producido un error')
else:
  print('La ejecuciòn continúa correctamente')
finally:
  print('Ejecutando finally')

try:
  print(numeroUno + numeroDos)
except ValueError as error:
  print(error)
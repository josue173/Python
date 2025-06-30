def mi_funcion():
  print("Primera función")

mi_funcion()

def sumar_dos_numeros(primer_numero, segundo_numero):
  print(primer_numero + segundo_numero)

sumar_dos_numeros(3,44242.15)
sumar_dos_numeros('333', '321321')

def retornar_dos_valores(uno, dos):
  return uno + dos

resultado = retornar_dos_valores(3,4)
print(resultado)

def print_nombre(nombre, apellido):
  print(f'{nombre} {apellido}')

print_nombre("Antony", "Toribio")
print_nombre(apellido = "Toribio", nombre = "Antony")

def print_nombre_por_defecto(nombre, apellido, alias = 'Sin datos'):
  print(f'{nombre} {apellido} {alias}')

print_nombre_por_defecto("Nombre", "Apellido")
print_nombre_por_defecto("Nombre", "Apellido", 'Con datos')

def print_textos(*textos):
  for texto in textos:
    print(texto)

print_textos('Hola','¿Cómo estás?')
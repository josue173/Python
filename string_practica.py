my_string = "Mi cadena"
my_other_string = 'Segunda cadena'

print(len(my_string))
print(len(my_other_string))
print(my_string, my_other_string)
print(my_string + my_other_string)

nueva_linea = "Nueva cadena \ncon salto de línea"
print(nueva_linea)

tabulacion = '\tCon tabulacion'
print(tabulacion)

scape = '\tString con \n escapado'
print(scape)

# DANDO FORMATO

nombre = 'Antony'
apellido = 'Toribio'
edad = 33

print('Mi nombre es {} {} y mi edad es {}'.format(nombre, apellido, edad))
print('Mi nombre es %s %s y mi edad es %d' %(nombre, apellido, edad))
print(f'Mi nombre es {nombre} {apellido} y mi edad es {edad}') # Inferencia de datos

# Desempaquetado de caracteres (es como la desestructuración en TS)

language = 'python'

a, b, c, d, e, f = language

print(a)
print(b)

# División

lenguaje_slice = language[1:3]
print(lenguaje_slice)

lenguaje_slice = language[1:]
print(lenguaje_slice)

lenguaje_slice = language[-4]
print(lenguaje_slice)

reversed_lan = language[0:6:5]
print(reversed_lan)

reversed_lan = language[::-1]
print(reversed_lan)


# Funciones

print(language.capitalize())
print(language.count("r"))
print(language.lower())
print(language.isnumeric())
print(language.isdecimal())
print(language.upper())
print(language.upper().isupper())
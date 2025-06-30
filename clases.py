class ClaseVacia:
  pass

print(ClaseVacia())

class Persona:
  def __init__(self, nombre, apellido, alias = 'Sin alias'):
    self.nombre = nombre
    self.apellido = apellido
    self.alias = f'({alias})'
    self.__alias2 = alias + ' private' # Propiedad privada

  def get_nombre (self):
    return self.__alias2
   
  def caminar(self):
    print(f'{self.nombre} {self.apellido} {self.alias} está caminando')

mi_persona = Persona('Antony', 'Toribio')
print(mi_persona.nombre, mi_persona.apellido)
mi_persona.caminar()
print(mi_persona.get_nombre())

otra_persona = Persona('Antony', 'Toribio', 'yo')
print(otra_persona.nombre, otra_persona.apellido)
otra_persona.caminar()
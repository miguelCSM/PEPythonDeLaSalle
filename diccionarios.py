# -*- coding: utf-8 -*-
"""
Un diccionario empieza con el concepto de conjunto (set) el cual sirve
para agrupar información por medio de categorías o significados afines
"""

#Declaramos el diccionario con key : value
diccionario = {
    'IDE': 'Integrated Developmet Environment',
    'OOP': 'Object Oriented Programing',
    'GPI': 'Gracias Por Invitar',
    'NTC': 'No Te Creas',
    'NTP': 'No te Preocupes',
    'key': 'value',
    'MLP': 'My Litle Pony'
    }

# Imprimir diccionario completo
#print(diccionario)

# Imprimir el diccionario por elementos
#print(diccionario['key'])

# Recorrer los diccionarios
for termino, valor in diccionario.items():
    print(termino,valor)

# Imprimir claves
for termino in diccionario.keys():
    print(termino)
# Imprimir Valores
for valor in diccionario.values():
    print(valor)

# Comprobar la existencia de algun elemento
print('MLP' in diccionario)  

# agregar elementos
diccionario['PK'] = 'Primary Key'

# remover elemento
diccionario.pop('IDE')

#limpiar el diccionario
diccionario.clear()

#Eliminar 
del diccionario
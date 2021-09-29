# -*- coding: utf-8 -*-
"""
Conjuntos declarados por {}
"""
planetas = {'Marte','Jupiter','Venus','Tierra'}

#imprimir el set
print(planetas)

# Saber el tañano de planetas
print(len(planetas))

#Verificar si un elemento forma parte del set
print('Venus' in planetas)

#agregar un elemento
planetas.add('Plutón')

#No repetir elementos
planetas.add('Marte')

#Eliminar elementos arrojando el error
planetas.remove('Tierra')

# Eliminar 
planetas.discard('Jupiter')
print(planetas)

#limpiar el set
planetas.clear()

#eliminar el set
del planetas
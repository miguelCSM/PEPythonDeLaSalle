# -*- coding: utf-8 -*-
""" Arreglos y uso de numpy """
import numpy as np
# arreglo unidimensional
la = [1,2,3]
a = np.array([1,2,3,4,5])
print(type(a)) # tipo de estructura
print(a.shape) # ver la forma filas y columnas
print(a[0],a[1],a[4]) # Acceder a los valores por medio de indice

#Asignar valor por medio del indice 
a[0]= 5

#Imprimir el arreglo completo
print(a)

# arreglos n-dimensionales/matrices
M = np.array([[1,2,3],[4,5,6],[7,8,9]])
f,c = M.shape

print(M[0,0])
print(M[2,2])
# Imprimir toda la columna 1
print(M[:,1])

# Imprimir toda la fila 
print(M[1,:])

# Declarar un arreglo de puros ceros
aCero = np.zeros((1,365))
aCero[0,364] = 19.5

# Declarar un arreglo de unos
aUnos = np.ones((2,2))

# Crear un arreglo n-dimensional con valores asignados
aPersonalizado = np.full((5,5),7)

#aAleatorio = np.random.random((5,5))
nA= np.random.randint(1, 10, (3, 3))
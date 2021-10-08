# -*- coding: utf-8 -*-
"""Arreglos parte 2"""

import numpy as np

arreglo = np.zeros([3,3])
filas,col = arreglo.shape

print(arreglo)

#Recorrer la fila
for i in range(0,filas):#Se mueve en filas 
    for j in range(0, col): # Se mueve en las columnas
        arreglo[i,j] = int(input())
        print(arreglo)


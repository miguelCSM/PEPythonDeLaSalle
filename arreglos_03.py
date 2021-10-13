# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 07:10:38 2021

@author: migue
"""

import numpy as np

vector = np.array([1, 2, 3])
sumaVector = vector.sum()
promedioVector = vector.mean()

matriz = np.array([[1,2,3],[4,5,6],[7,8,9]])

# Accede a la fila 1 de la matriz y se calcula el promedio
print(matriz[1,:].mean())

filas, col = matriz.shape

for i in range(0,filas):
    print(matriz[i,:])
    print('\t',matriz[i,:].mean())
    
a = np.arange(1000)



















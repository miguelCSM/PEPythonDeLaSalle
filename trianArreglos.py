# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 07:41:52 2021

@author: migue
"""

# Ejercicio En un arreglo guardarán las medidas de los lados de
# n-triangulos indicados por el usuario. Requieren capturar el tamaño
# de cada lado y el tipo de triangulo que resulta.

#1. Saber cuantos triangulos (input)
#2. Declarar la matriz y asignar el tamaño
#3. Guardar en la matriz el valor de los lados de cada triangulo
#4. Calcular el tipo de triangulo

# Captura el numero de triangulos
import numpy as np
nTriangulos = int(input("Cuantos triángulos desea almacenar?"))
nLados = 3

matriz = np.zeros([nTriangulos,nLados])

for i in range(0,nTriangulos):
    for j in range(0,nLados):
        print("Triangulo" , i+1, "lado", j+1)
        matriz[i,j] = int(input())
        
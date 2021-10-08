# -*- coding: utf-8 -*-
"""Arreglos parte 2"""

import numpy as np

arreglo = np.zeros([2,3])
filas,col = arreglo.shape

print(arreglo)

#Recorrer la fila y columnas
for i in range(0,filas):#Se mueve en filas 
    for j in range(0, col): # Se mueve en las columnas
        print("Posición",i,", ",j)
        arreglo[i,j] = int(input()) # Guardar el valor en la posicion fil,col
        print(arreglo)

# Recorremos Columnas y filas
for i in range(0,col):#Se mueve en filas 
    for j in range(0, filas): # Se mueve en las columnas
        print("Posición",i,", ",j)
        arreglo[j,i] = int(input()) # Guardar el valor en la posicion fil,col
        print(arreglo)
        
#%% Ejercicio        
# Diseñar un programa que permita capturar n- calificaciones 
# correspondientes a n alumnose imprimir los promedios por alumno
import numpy as np

alumnos = int(input("Cuántos alumnos?\n"))
calificaciones = int(input("Cuántas calificaciones?\n"))

mCalif = np.zeros([alumnos,calificaciones])

# Capturamos matriz 
for i in range(0,alumnos):
    for j in range(0,calificaciones):
        print("Alumno:",i,"Calificacion:",j)
        mCalif[i,j] = int(input())
        
for i in range(0,alumnos):
    print(mCalif[i,:].mean())
    

# -*- coding: utf-8 -*-
"""
Funciones Parte II
"""

#Diseñar un función que reciba el numero de calificaciones para 
# calcular promedio. Tambien recibe el tipo de alumno que es, si es alumno 
#regular se le dan 0.5 puntos extras y en caso contrario se le restan 0.5 puntos

def calculaPromedio(nCalif, tipoA):
    suma = 0
    tipo = ""
    for i in range(1,nCalif+1):
        print("Calificación:",i)
        calif = float(input())
        suma += calif
    promedio = suma/nCalif
    if (tipoA ==1):
        tipo = "Regular"
        promedio += 0.5
    else:
        tipo = "Irregular"
        promedio -= 0.5
    #print("El promedio del alumno de tipo",tipo, "es:", promedio)
    return promedio, tipo # devuelve los valores declarados dentro de la funcion

promedio, tipo = calculaPromedio(2, 1)
print("El promedio del alumno de tipo",tipo, "es:", promedio)

# Diseña una función que le permita calcular el volumen de un cilindro

def voluC(r,h):
    import math as mt
    V = (mt.pi*mt.pow(r, 2))*h
    print("El volumen es de", V)
    return V

volumen = voluC(10, 10)























# -*- coding: utf-8 -*-
#Warm up lists
""" Métodos para trabajar con listas """

listaVacia = [];# Cualquier tipo de elemento puede ser guardado
numeros = [1,2,3,4,5]# Para identificar un elemento este separa con coma
caracteres = ["a","b","c"]
mixtas = [1,True,"cadena", 1.14]

# Una lista no es restrictiva del tipo de dato

#Métodos para usar lista
#Agregar elementos de una lista
listaVacia.append("Guanajuato")
listaVacia.append("León")

# Inserter elemento en un indice especifico 
listaVacia.insert(1, "San Felipe")

# Remover elemento por nombre
#listaVacia.remove("Guanajuato")

# Remover elemento por indice
#del listaVacia[2]

#Remover el ultimo valor de la lista
#listaVacia.pop()

#Limpiar lista
#listaVacia.clear()

#Eliminar lista
#del listaVacia
"""Programa que solamente permita guardar numeros 
enteros en la lista"""

numeros = []#Acepta puros numeros
capturar = "no"


capturar = input("Desea capturar una lista de numeros?")

while(capturar == "si"):
    dato = input("Ingrese dato que sea entero")
    datoEntero = int(dato)
    numeros.append(datoEntero)
    capturar = input("Desea capturar un numero más?")
    
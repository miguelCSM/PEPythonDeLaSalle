# -*- coding: utf-8 -*-
"""
Ejercicio de diccionario 

"""
import operator 
d = {1:2,3:4,4:3,2:1,0:0}

print("Diccionario original: ", d)

dOrd = sorted(d)

d[5] = 15
#%% Ejercicio

# Agregar a un diccionario de dependencias de gobierno y sus siglas
agregar = input("Desea agregar?")
diccionario ={}

while(agregar == "si"):
    llave = input("\nSigla:\t")
    valor = input("\nValor\t")
    diccionario[llave]=valor
    agregar = input("Desea agregar otro elemento?")    
    
print(diccionario)
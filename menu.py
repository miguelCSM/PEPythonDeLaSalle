# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 08:08:07 2021

@author: migue
"""

# Calcular la serie de Fibonnacci

t1 = 0
t2 = 1

nTerminos = int(input("Digite el numero de termines de la serie de Fibonacci"))

print(t1)
print(t2)
for i in range(nTerminos-2):
    # Se calcula el término nuevo
    tn = t1+t2
    print(tn)
    # Se actualizan los términos
    t1 = t2
    t2 = tn
    
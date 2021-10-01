# -*- coding: utf-8 -*-
"""
Ejemplo diccionario
"""
#%% lista
import time 
start_time = time.time()

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



for i in lista:
    print(i)
    
print("segundos" , (time.time()-start_time))

#%%Diccionario
diccionario = {'1':1,'2':2,'3':3,'4':4,'5':5,}
print(diccionario)
print("segundos" , (time.time()-start_time))
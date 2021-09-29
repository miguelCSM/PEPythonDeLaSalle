# -*- coding: utf-8 -*-
"""
Ciclos - continue y break
"""
#%% For controlado por una cadena
for i in "PALABRAS":
    print(i)
    
#%% For controlado por una lista
lista = ["Miguel", 1, 3.14, True]

for i in lista:
    print(i)
    
#%% For controlado por la funcion range(stop)
for i in range(5):
    print(f'Valor: {i}')

#%% For controlado por la funcion range (start, stop, step)
for i in range(1,6,2):
    print(f'valor: {i}')

#%% Imprimir los numeros pares que hay de 0 a 6

for i in range(7):
    if i%2 == 0:
        #print(f'Valor: {i}')
        print("Valor",i)
        
#%% Imprimir impares
for i in range(7):
    if i%2 != 0:
        print(f'Impar : {i}')
        if i ==3:
            break# Romper el ciclo y salir bloque de instrucciones
print("Ya estoy fuera del ciclo for")

#%% El uso de la palabra reservada continue - imprimir numeros pares
for i in range(6):
    if i % 2 != 0:
        continue
    print(f'Valor: {i}')
    

#%%
agregar = "no"
usuarios =[]# nombres
edades = [] # edades
estados = [] # mayor o menor

agregar = input("Desea agregar un usuario nuevo? Responda si o no")

while(agregar == "si"):
    nombre = input("Cual es el nombre?")
    usuarios.append(nombre)
    edad = int(input("Cual es la edad?"))
    edades.append(edad)
    if (edad >=18):
        print("Mayor")
        estados.append("Mayor")
    else: 
        print("Menor")
        estados.append("Menor")
    agregar = input("Desea agregar otro usuario nuevo? Responda si o no")    
    

# Imprimir cada uno de los usuario con sus edad y estados correspondientes

for i in range(len(usuarios)):
    print(f'Usuario: {usuarios[i]} y su edad {edades[i]} y es {estados[i]}')







# -*- coding: utf-8 -*-
"""
Colecciones - Listas
"""
#Declarar lista Str
nombres = ["Juan", "Karla", "Ricardo", "María"]

# Imprimir lista
print(nombres)

#Acceder elementos de una lista por su indice
print(nombres[0])
print(nombres[3])

# Acceder a un rango de elementos
print(nombres[0:3])

#Imprimir desde el inicio hasta el indice indicado
print(nombres[:3])

# desde el indice seleccionado hasta el final
print(nombres[1:])

#%%Modificar el valor de un elemento de la lista

nombres[2] = "Daniela"
nombres[0] = "Benito Juárez"

for nombre in nombres:
    print(nombre)
else:
    print("No existen más nombres en la lista")
#%% Largo de una lista
print(len(nombres)) # Len permite saber el tamaño de una lista

#%% Agregar elemento a la lista
nombres.append("Jaime Krauss") # append agrega al final el elemento

#%% Ejemplo de 3 listas
cliente = ["Maribel", "Daniela", "Isabella", "Hayde"]
edad = [18,18,18,18]
direccion = ["Campestre", "Cañada", "G. Jardín", "R. NAranjos"]

for i in range(len(cliente)):
    print(f'Cliente : {cliente[i]} Direccion : {direccion[i]} Edad: {edad[i]}')

#%% En una lista vacía guarda las calificaciones de un alumno, indicando el numero calif
calificaciones = []
promedio = 0

nCalif = int(input("Cuantas calificaciones desea guardar?\n"))

for i in range(nCalif):
    print(f'Calificacion {i}')
    calif = float(input())
    calificaciones.append(calif)
    promedio += calif
    
promedio = promedio/nCalif
print(calificaciones, " y su promedio = ", promedio)



















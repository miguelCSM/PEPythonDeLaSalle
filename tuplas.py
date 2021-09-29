# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 07:38:18 2021

@author: migue
"""

# Tupla -> nombreTupla = (elemento1, elemento, ..., elementon)
frutas = ('Naranja', 'Platano', 'Guayaba')

print(frutas)

#Saber longitud de la tupla
print("Esta tupla tiene una longitud de",len(frutas))

# Acceder a un elemento
print(frutas[2])

# Acceder a un rango de elementos
#print(frutas[0:2])

# Asignar por medio una tupla el estado civil de un empleado

# estaC = ('Soltero', 'Unión Libre','Casado', 'Divorciado', 'Viudo')

# usuario = []

# nombre = input("Ingrese su nombre")
# edad = int(input("ingrese su edad"))
# estadoCivil = int(input("\n Seleccione el numero que corresponda \n1. Soltero \n2. Union Libre \n3. Casado \n4. Divorciado \n5. Viudo"))

# usuario.append(nombre)
# usuario.append(edad)
# usuario.append(estaC[estadoCivil-1])

# print(usuario)


# recorrer elementos de la tupla
for fruta in frutas:
    print(fruta, end=' - ')
    
#Cambiar elemento de una tupla
#frutas[0] = 'Pera'
frutasLista = list(frutas) # Se hace conversion de tupla a lista
frutasLista[0] = 'Pera' # Se agrega el elemento
frutas = tuple(frutasLista) # Se hace conversión de lista a tupla


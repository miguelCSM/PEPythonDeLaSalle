# -*- coding: utf-8 -*-
"""
Funciones
"""
#Declaración de función
def saludar():# si la funcion es vacia entonces no recibe ningun parametro
    # Instrucciones de la función
    print("Hola, bienvenidos al curso de programación estructurada")

#Ejecutamos la función o haciendo el llamado de ella
#saludar()

# Argumentos, estos permiten enviar parametros de entrada y procesarlos
def saludarPersona(nombre):
    print("Bienvenido", nombre)
    
#saludarPersona("Krauss")

# Función suma de dos numeros 
def suma(numero1, numero2):
    res = numero1+numero2
    print("suma =", res)
    return res # sirve para devolver un valor que se requiera guardar

resultado = suma(15,15)

# Diseñar un función para calcular el area de distintos tipos de figuras
# Cuadrado, Triangulo y el circulo

def area(tipoFigura):
    #Cuadrado
    if(tipoFigura==1):
        tipo = "Cuadrado"
        lado = float(input("Lado"))
        Area = lado*lado
        print("El area del ",tipo, "es igual a:",Area)
        return Area
    # Triangulo
    if(tipoFigura==2):
        tipo = "Triangulo"
        base = float(input("Base:"))
        altura = float(input("Altura"))
        Area = (base*altura/2)
        print("El area del", tipo, "es igual a", Area)
        return Area
    # Circulo
    if(tipoFigura==3):
        tipo = "Circulo"
        radio = float(input("Radio:"))
        import math as mt
        Area = 3.1416 * mt.pow(radio, 2)
        print("El area del",tipo,"es igual a", Area)
        return Area
    
#resultado = area(3)

# Diseñar una función que reciba como parametro un numero
# e imprimar la tabla correspondiente del 1 al 10
def tabla(numero):
    # Instrucciones
    for i in range(1,11):
        print(numero,"X",i,"=",i*numero)
        
# Diseñar un funcion que reciba como parametros
# a,b y c para calcular las raices de una ecuación cuadrática
def chicharronero(a,b,c):
    
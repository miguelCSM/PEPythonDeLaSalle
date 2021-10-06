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
        lado = float(input("Ingrese el valor de un lado para calcular el area del cuadrado"))
        Area = lado*lado
        print("El area del ",tipo, "es igual a:",Area)
        return Area
    
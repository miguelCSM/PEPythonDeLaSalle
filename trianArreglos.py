# -*- coding: utf-8 -*-

# Ejercicio En un arreglo guardarán las medidas de los lados de
# n-triangulos indicados por el usuario. Requieren capturar el tamaño
# de cada lado y el tipo de triangulo que resulta.

#1. Saber cuantos triangulos (input)
#2. Declarar la matriz y asignar el tamaño
#3. Guardar en la matriz el valor de los lados de cada triangulo
#4. Calcular el tipo de triangulo

# Captura el numero de triangulos
import numpy as np
nTriangulos = int(input("Cuantos triángulos desea almacenar?"))
metodo = int(input("Por cual método gusta clasificar 1. Lados 2. Ángulos"))

nLados = 3
tipos = []
matriz = np.zeros([nTriangulos,nLados])

if (metodo == 1):
    # Almacenan los lados 
    for i in range(0,nTriangulos):
        for j in range(0,nLados):
            print("Triangulo" , i+1, "lado", j+1)
            matriz[i,j] = int(input())
    
    for i in range(0,nTriangulos):
        if(matriz[i,0] == matriz[i,1] and matriz[i,0] == matriz[i,2]):
            tipos.append("Equilatero")
        elif (matriz[i,0]==matriz[i,1] or matriz[i,1]==matriz[i,2] or matriz[i,0]== matriz[i,2]):
            tipos.append("Isosceles")
        else:
            tipos.append("Escaleno")
        
elif (metodo == 2):
    for i in range(0,nTriangulos):
        for j in range(0,nLados):
            print("Triangulo" , i+1, "Ángulo", j+1)
            matriz[i,j] = int(input())
        suma = matriz[i,:].sum()
        
        #if (suma != 180):
        while(suma!= 180):
            suma = 0
            for j in range(0,nLados):
                print("Tienes que repetir la captura del tringulo")
                print("Triangulo" , i+1, "Ángulo", j+1)
                matriz[i,j] = int(input())
                
            
            
    for i in range(0,nTriangulos):
        if(matriz[i,0]==90 or matriz[i,1]==90 or matriz[i,2]==90):
            tipos.append("Rectángulo")
        elif (matriz[i,0]<90 and matriz[i,1]<90 and matriz[i,2]<90):
            tipos.append("Acutángulo")
        else:
            if (matriz[i,0]>90 and matriz[i,0]<180 or matriz[i,1]>90 and matriz[i,1]<180 or matriz[i,2]>90 and matriz[i,2]<180):
                tipos.append("Obtusángulo")
                
                

        
        
        
        
        
        
        
        
        
        
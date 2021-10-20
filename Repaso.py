# -*- coding: utf-8 -*-
""" Desarrolle un programa en Python quer permita reconocer la temperatura 
promedio semanal con base en la captura de los datos climatológicos y permita
predecir como se encontrará la siguiente semana con base en las siguientes 
reglas:
    Si persiste el promedio con temperaturas entre:
        menor a 23 -> Frio
        23 y 30 grados -> Templado 
        31 en adelante -> Caluroso
Deberan indicar al usuario la categoría por día y la predicción del clima 
de la siguiente semana con base en el promedio, el programa se podrá
ejecutar mientras el usuario así lo desee"""
import numpy as np

dias = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']

temp = np.zeros([7,1])
continua = input("Desea predecir el clima de la siguiente semana Si o No")

while(continua == "si" or continua == "SI" or continua == "Si" or continua == "sI"):
    for i in range(len(dias)):
        print("Ingrese temperatura del día", dias[i])
        temp[i] = input()
        if (i>0):
            diferencia = abs(temp[i-1]-temp[i])
            while(diferencia >=10):
                print("Es valida la temperatura actual de ", temp[i],"?")
                continua = input("Si o no")
                if (continua== "no"):
                    print("Ingrese nuevamente la temperatura del día", dias[i])
                    temp[i] = input()
                    diferencia = abs(temp[i-1]-temp[i])   
                else:
                    break
        
    for i in range(len(dias)):
        if(temp[i]<23):
            print(dias[i], temp[i],"° = Frio")
        elif(temp[i]>=23 and temp[i]<=30):
            print(dias[i], temp[i],"° = Templado")
        else:
            print(dias[i], temp[i],"° = Caluroso")
          
    promedio = temp.mean()
    
    if (promedio < 23):
        print("La próxima semana habrá temperaturas menores a 23°, clima frio")
    elif (promedio >= 23 and promedio <= 30):
        print("La próxima semana habrá temperaturas entre los a 23 y 30°, clima templado")
    else:
        print("La próxima semana habrá temperaturas mayores a 30°, clima caluroso")
    
    continua = input("Desea predecir nuevamente el clima de la siguiente semana Si o No")
    

""" Si la variación de temperaturas entre cada día es mayor o igual a 
10 grados deberán solicitar la confirmación de esta o el cambio de clima"""









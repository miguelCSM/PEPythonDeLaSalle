# -*- coding: utf-8 -*-
"""
Librerias
"""
# Math
import math as mt
import random as rd

#nAleatorio = rd.random()

nAleatorio = rd.randint(1, 5)

# Quien es mayor -> Dos jugadores se tiraran 5 veces dos dados
# y quien tenga la mayor puntuación ganará o quien llegue primero a 30
dado1 = 0
dado2 = 0
score1 = 0
score2 = 0

rondas = int(input("Cuantas rondas van a jugar?"))
for i in range(rondas):
    print("\nRonda #",i+1)
    print("\nEs tiempo del jugador 1")
    jugar = input("\nDesea tirar sus dados")
    if(jugar == "si"):
        dado1 = rd.randint(1, 6)
        print("\nDado 1",dado1)
        dado2 = rd.randint(1, 6)
        print("\nDado 2:",dado2)
        score1 += dado1 +dado2
    print("\nEs tiempo del jugador 2")
    jugar = input("\nDesea tirar sus dados")
    if(jugar == "si"):
        dado1 = rd.randint(1, 6)
        print("\nDado 1",dado1)
        dado2 = rd.randint(1, 6)
        print("\nDado 2:",dado2)
        score2 += dado1 +dado2
    print("\nPts Jugador 1:",score1,"\nPts Jugador 2:", score2)
    if(score1 >=30):
        print("El jugador 1 ganó")
        break
    if(score2>=30):
        print("El jugador 2 ganó")
        break

if (score1>score2):
    print("El jugador 1")
elif (score2==score1):
    print("Empate")
else:
    print("El jugador 2")
        
        
    
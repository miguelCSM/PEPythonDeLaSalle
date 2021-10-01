# -*- coding: utf-8 -*-
"""
Juego de Serpientes y Escaleras
"""
import random as rd
s = {11:3,23:16,25:20,35:28}
e = {6:18,12:19,15:27}
score1 = 0
score2 = 0

print("VAMOS A COMENZAR EL JUEGO DE S. Y E.")
while (score1<=35 or score2<=35):
    # Jugador 1
    print("Jugador 1")
    dado1 = rd.randint(1, 6)    
    dado2 = rd.randint(1, 6) 
    score1 += dado1+dado2
    if(score1 in e):
        score1 = e[score1]
    if(score1 in s):
        score1 = s[score1]
    print(score1)
    #Jugador 2
    print("Jugador 2")
    dado1 = rd.randint(1, 6)    
    dado2 = rd.randint(1, 6) 
    score2 += dado1+dado2
    if(score2 in e):
        score2 = e[score2]
    if(score2 in s):
        score2 = s[score2]
    print(score2)
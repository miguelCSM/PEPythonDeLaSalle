# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 07:30:42 2021

@author: migue
"""

from tkinter import *

MiLista = ["Miguel", "Krauus", "Maribel"]
edadLista = [21,18,17]

window = Tk()

window.title("Control de inventarios")

window.geometry("600x300")

xP = 0
yP = 0

for i in range(len(MiLista)):
    nombre = MiLista[i]
    lbl1 = Label(window, text= nombre)
    lbl1.place(x=xP, y=yP)
    edad = edadLista[i]
    lbl2 = Label(window, text= edad)
    lbl2.place(x=100, y=yP)
    yP +=50
    

window.mainloop()
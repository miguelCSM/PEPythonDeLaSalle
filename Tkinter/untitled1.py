# -*- coding: utf-8 -*-
"""
Desarrollar un programa en Python que permita guardar
en una lista 3 calificaciones de n-alumnos
haciendo uso de 3 entradas de texto.

Colocar boton de agregar y boton de mostrar
"""
import numpy as np
from tkinter import *

window =  Tk()

# objeto de tipo funcion que manda llamar propiedades
window.title("Calificaciones")
window.geometry("500x250")

Lcal1 = []
Lcal2 = []
Lcal3 = []

def add():
    Lcal1.append(cal1.get())
    Lcal2.append(cal2.get())
    Lcal3.append(cal3.get())
    print(Lcal1,Lcal2,Lcal3)

lbl1 = Label(window, text= "Calif. 1")
lbl1.place(x=0, y=0)

cal1 = Entry(window)
cal1.place(x=0,y=20)

lbl2 = Label(window, text= "Calif. 2")
lbl2.place(x=0, y=40)

cal2 = Entry(window)
cal2.place(x=0,y=60)

lbl3 = Label(window, text= "Calif. 3")
lbl3.place(x=0, y=80)

cal3 = Entry(window)
cal3.place(x=0,y=100)

btnAdd = Button(window, text= "Agregar", command = add)
btnAdd.place(x = 0, y = 130)

btnCalc = Button(window, text= "Promedios", command = "")
btnCalc.place(x = 80, y = 130)

window.geometry("500x250")
window.mainloop()  
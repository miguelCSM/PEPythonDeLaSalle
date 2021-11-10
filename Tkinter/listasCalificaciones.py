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
    Lcal1.append(float(cal1.get()))
    Lcal2.append(float(cal2.get()))
    Lcal3.append(float(cal3.get()))
    # Limpiar entradas
    cal1.delete(0,END)
    # cal1.insert(0,"0")
    cal2.delete(0,END)
    cal3.delete(0,END)
    
    #print(Lcal1,Lcal2,Lcal3)

def promedio():
    cols = 3
    rows = len(Lcal1)
    
    # convertir lista en arreglo
    arr1 = np.asarray(Lcal1)
    arr2 = np.asarray(Lcal2)
    arr3 = np.asarray(Lcal3)
    
    #creamos una matriz de calificaciones
    matriz = np.array([arr1,arr2,arr3])  
    prom1 = matriz[0,:].mean()        
    
    print(matriz, type(matriz), prom1)
    
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

promedios = Label(window, text= "Promedios")
promedios.place(x=280,y=20)

p1lbl =  Label(window, text = "Periodo 1")
p1lbl.place(x= 150,y=40)

p2lbl =  Label(window, text = "Periodo 2")
p2lbl.place(x= 280,y=40)

p3lbl =  Label(window, text = "Periodo 3")
p3lbl.place(x= 430,y=40)

btnAdd = Button(window, text= "Agregar", command = add)
btnAdd.place(x = 0, y = 130)

btnCalc = Button(window, text= "Promedios", command = promedio)
btnCalc.place(x = 80, y = 130)

window.geometry("500x250")
window.mainloop()  
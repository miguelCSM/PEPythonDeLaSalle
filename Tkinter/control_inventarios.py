# -*- coding: utf-8 -*-
"""
Diseñar una GUI que permita buscar en una lista un prod.
por medio del id_producto.
"""
from tkinter import *

id_prod = ["001","002","003","004","005"]
d_prod = ["Tenis", "Sandalias", "Zapatilla","Tachones","Pantunflas"]
p_prod = [100.0, 20.0, 30.0,200.0,10.0]
p_cant = [10,15,5,2,100]

mensaje = ""

def buscar():
    indBuscado = id_prod.index(idB.get())
    mensaje = indBuscado
    print(mensaje)
    lblMensaje.configure(text = mensaje)    

window = Tk()

window.title("Control de inventarios")

window.geometry("600x300")

lbl1 = Label(window, text= "ID Producto")
lbl1.place(x=0, y=0)

idB = Entry(window)
idB.place(x=0,y=20)

lblMensaje = Label(window, text= "")
lblMensaje.place(x=0, y=100)

btnAdd = Button(window, text= "Buscar", command = buscar)
btnAdd.place(x = 0, y = 40)

window.mainloop()
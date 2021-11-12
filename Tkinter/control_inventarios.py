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
    indBuscado = (idB.get())
    if indBuscado in id_prod:
        iB = id_prod.index(indBuscado)
        mensaje = "El producto si existe"
        print(mensaje)
        lblMensaje.configure(text = mensaje)
        
        lblDescrip = Label(window, text="")
        lblDescrip.place(x = 0,y=80)
        lblDescrip.configure(text = d_prod[iB])
        
        lblPrecio = Label(window, text  = "")
        lblPrecio.place(x=0,y=100)
        lblPrecio.configure(text = p_prod[iB])
        
        lblCantidad = Label(window, text  = "")
        lblCantidad.place(x=0,y=120)
        lblCantidad.configure(text = p_cant[iB])
        
        elementsCompra()
        
    else:
        mensaje = "No Existe el Producto"
        lblMensaje.configure(text = mensaje) 
        
def elementsCompra():    
    lblpiezas = Label(window, text= "Piezas")
    lblpiezas.place(x = 150,y=160)
    
    cantCompra = Entry(window)
    cantCompra.place(x = 150, y = 180)
    
    comprarbtn = Button(window, text= "Comprar")
    comprarbtn.place(x = 150,y = 200)
    
print(iB)

window = Tk()

window.title("Control de inventarios")

window.geometry("600x300")

lbl1 = Label(window, text= "ID Producto")
lbl1.place(x=0, y=0)

idB = Entry(window)
idB.place(x=0,y=20)

lblMensaje = Label(window, text= "")
lblMensaje.place(x=0, y=60)

btnAdd = Button(window, text= "Buscar", command = buscar)
btnAdd.place(x = 0, y = 40)

window.mainloop()
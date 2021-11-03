# -*- coding: utf-8 -*-
from tkinter import *

window =  Tk()

# objeto de tipo funcion que manda llamar propiedades
window.title("Tipos de triángulo")
window.geometry("350x200")

lbl1 = Label(window, text= "Lado a")
lbl1.place(x=0, y=0)

lbl2 = Label(window, text= "Lado b")
lbl2.place(x=125, y=0)

lbl3 = Label(window, text= "Lado c")
lbl3.place(x=250, y=0)

ladoA = Entry(window)
ladoA.place(x=0,y=30)

ladoB = Entry(window)
ladoB.place(x=125,y=30)

ladoC = Entry(window)
ladoC.place(x=250,y=30)

resultado = Label(window, text= "Resultado")
resultado.place(x = 250, y = 60)



def calcular():    
    prueba = float(ladoC.get())/float(ladoA.get())
    print(prueba)
    if(ladoA.get() == ladoB.get() and ladoB.get()==ladoC.get()):
        res = "Equilatero"
    elif(ladoA.get() == ladoB.get() or ladoB.get() == ladoC.get() or ladoA.get() == ladoC.get()):
        res = "Isosceles"
    else:
        res = "Escaleno"
    resultado.configure(text=res)
    
btn = Button(window, text= "calcular", command = calcular)
btn.place(x = 125, y = 60)


window.geometry("500x250")
window.mainloop()  # Permite ejecutar indefinidamente el programa
  
# -*- coding: utf-8 -*-

from tkinter import *

window =  Tk()

window.title("Hello")
window.geometry("350x200")

lbl1 = Label(window, text= "Num 1")
lbl1.place(x=0, y=0)

lbl2 = Label(window, text= "Num 2")
lbl2.place(x=250, y=0)

num1 = Entry(window)
num1.place(x=0,y=30)

num2 = Entry(window)
num2.place(x=250,y=30)

def clicked():
    res = int(num1.get()) - int(num2.get())
    lbl3.configure(text=res)
    
lbl3 = Label(window)
lbl3.place(x=0, y=90)
    
btn = Button(window,text="Sumar", command = clicked)

btn.place(x=0,y=120)
window.geometry("500x250")
window.mainloop()   
# -*- coding: utf-8 -*-

from tkinter import *

window =  Tk()

window.title("Hello")
window.geometry("350x200")

lbl = Label(window, text= "Hello")
lbl.place(x=0, y=0)

txt = Entry(window)
txt.place(x=0,y=30)

def clicked():
    lbl.configure(text="Hello " + txt.get())
    
btn = Button(window,text="touch me", command = clicked)

btn.place(x=0,y=60)

window.mainloop()   
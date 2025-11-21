import tkinter
from tkinter import *

bag = []

def add(event = None):
    bag.append(input_text.get())
    input_text.delete(0, tkinter.END)
    text_box.delete(1.0, tkinter.END)
    text_box.insert(tkinter.END, "\n".join(bag)+"\n")

def rem(event = None):
    bag.remove(input_text.get())
    input_text.delete(0, tkinter.END)
    text_box.delete(1.0, tkinter.END)
    text_box.insert(tkinter.END, "\n".join(bag)+"\n")

main = tkinter.Tk()

title = Label(main, text="Välkommen till påsen")
title.pack()

input_text = tkinter.Entry(main)
input_text.pack()

add_button = tkinter.Button(main, text="Lägg till", command=add)
add_button.pack()

rem_button = tkinter.Button(main, text="Ta bort", command=rem)
rem_button.pack()

text_box = tkinter.Text(main, height=10)
text_box.pack()

quit_button = tkinter.Button(main, text="Avsluta", command=quit)
quit_button.pack()

main.mainloop()
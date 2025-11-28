import tkinter
from tkinter import *

bag = []
button_name = ["Lägg till", "Ta bort"]

def add(event = None):
    text_box.delete(1.0, tkinter.END)
    if option.get() == 0:
        bag.append(input_text.get())
    elif option.get() == 1:
        bag.remove(input_text.get())
    text_box.insert(tkinter.END, "\n".join(bag)+"\n")
    input_text.delete(0, tkinter.END)

main = tkinter.Tk()

title = Label(main, text="Välkommen till påsen")
title.pack()

option = IntVar()
Radiobutton(main, text="Lägg till", variable=option, value=0).pack(anchor=W)
Radiobutton(main, text="Ta bort", variable=option, value=1).pack(anchor=W)

input_text = tkinter.Entry(main)
input_text.pack()

add_button = tkinter.Button(main, text=button_name[0] , command=add)
add_button["text"] = button_name[option.get()]
add_button.pack()


text_box = tkinter.Text(main, height=10)
text_box.pack()

quit_button = tkinter.Button(main, text="Avsluta", command=quit)
quit_button.pack()

main.mainloop()
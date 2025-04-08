import tkinter as tk
from tkinter import *
from tkinter import ttk

window =tk.Tk()
window.title("POKEMON ADVENTURE")
window.geometry("675x575")

mainmap = PhotoImage(file="main.png")
minimap = PhotoImage(file="minimap.png")
nintendo = PhotoImage(file="logo.png")

label1 = tk.Label(window, image=mainmap, borderwidth=2, relief="ridge")
label2 = tk.Label(window, image=minimap)
label3 = tk.Label(window, image=nintendo)
label4 = tk.Label(window, text="MINI MAP")
button1 = tk.Button(window, text="MAP",width=13, height=2, anchor="center")
button2 = tk.Button(window, text="INVENTORY",width=13, height=2, anchor="center")
button3 = tk.Button(window, text="POKEDEX",width=13, height=2, anchor="center")
button4 = tk.Button(window, text="ROSTER",width=13, height=2, anchor="center")
button5 = tk.Button(window, text="JOURNAL",width=13, height=2, anchor="center")
button6 = tk.Button(window, text="HELP",width=13, height=2, anchor="center")
button7 = tk.Button(window, text="SHOP",width=13, height=2, anchor="center")
button8 = tk.Button(window, text="NW", width=3, height=1)
button9 = tk.Button(window, text="N", width=3, height=1, borderwidth=2, relief="raised")
button10 = tk.Button(window, text="NE", width=3, height=1)
button11 = tk.Button(window, text="W", width=3, height=1, borderwidth=2, relief="raised")
button12 = tk.Button(window, text="E", width=3, height=1, borderwidth=2, relief="raised")
button13 = tk.Button(window, text="SW", width=3, height=1)
button14 = tk.Button(window, text="S", width=3, height=1, borderwidth=2, relief="raised")
button15 = tk.Button(window, text="SE", width=3, height=1)


label1.place(x=25,y=25)
label2.place(x=540, y=75)
label3.place(x=280, y=490)
label4.place(x=559, y=50)
button1.place(x=540,y=175)
button2.place(x=540,y=215)
button3.place(x=540,y=255)
button4.place(x=540,y=295)
button5.place(x=540,y=335)
button6.place(x=540,y=375)
button7.place(x=540,y=415)
button8.place(x=25, y=475)
button9.place(x=55, y=475)
button10.place(x=85, y=475)
button11.place(x=25, y=500)
button12.place(x=85, y=500)
button13.place(x=25, y=525)
button14.place(x=55, y=525)
button15.place(x=85, y=525)



window.mainloop()
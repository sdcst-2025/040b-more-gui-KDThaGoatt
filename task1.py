import tkinter as tk
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("tk")
window.geometry("400x90")

label1 = tk.Label(window, text="Principal")
label2 = tk.Label(window, text="Interest Rate")
label3 = tk.Label(window, text="Years")
label4= tk.Label(window, text="-")
label5= tk.Label(window, text="Amount")
entry1 = tk.Entry(window, width=22)
entry2 = tk.Entry(window, width=23)
entry3 = tk.Entry(window, width=22)
combo1 = ttk.Combobox(window, width=18)

label1.place(x=40, y=5)
label2.place(x=165, y=5)
label3.place(x=315, y=5)
label4.place(x=60, y=45)
label5.place(x=80, y=70)
entry1.place(x=0, y=25)
entry2.place(x=133, y=25)
entry3.place(x=133, y=70)
combo1.place(x=269, y=25)

window.mainloop()
# tkinter_label.py

from tkinter import *

oroot = Tk()
olabel1 = Label(oroot, text="적", bg="red", width=20)
olabel2 = Label(oroot, text="녹", bg="green", width=20)
olabel3 = Label(oroot, text="파", bg="blue", width=20)

olabel1.pack()
olabel2.pack()
olabel3.pack()
oroot.mainloop()

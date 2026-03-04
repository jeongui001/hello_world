# tkinter_button2.py

from tkinter import *

oroot = Tk()
oroot.geometry("200x200+0+0")
obutton1 = Button(oroot, text="push1")
obutton2 = Button(oroot, text="push2")
obutton3 = Button(oroot, text="push3")
obutton1.pack()
obutton2.pack()
obutton3.pack()
oroot.mainloop()

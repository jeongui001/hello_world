# image_widget.py

from tkinter import PhotoImage, Tk, Label, Button

oroot = Tk()
oroot.geometry("800x6   00")
img1 = PhotoImage(file="ch11/image_dog.png")
img_label = Label(oroot, image=img1)
img_label.place(x=0, y=0)

obutton1 = Button(oroot, text="PUSH1")
obutton2 = Button(oroot, text="PUSH2")
obutton3 = Button(oroot, text="PUSH3")
obutton1.place(x=10, y=60)
obutton2.place(x=140, y=60)
obutton3.place(x=80, y=10)

oroot.mainloop()
# C:\rokey\py_work\ch11

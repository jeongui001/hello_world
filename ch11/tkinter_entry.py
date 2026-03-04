# tkinter_entry.py

from tkinter import *

# Entry위젯
oroot = Tk()
ostring = StringVar()  # str 문자열
oentry = Entry(
    oroot, textvariable=ostring
)  # 엔트리 생성, 윈도우창 = oroot, 텍스트 = str문자열
oentry.pack()  # 윈도우창에 올리기(활성화)
olebel = Label(
    oroot, textvariable=ostring
)  # 라벨 생성, 윈도우창 = oroot, 텍스트 = str문자열
olebel.pack()
oroot.mainloop()

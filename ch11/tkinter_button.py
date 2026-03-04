# tkinter_button.py

from tkinter import *  # tkinter 모듈 임포트


def hello():
    print("hello")


otk = Tk()  # 윈도우창 객체 생성
otk.geometry("100x150+0+0")  # 윈도우창 객체 크기 및 위치 설정(0,0은 왼쪽 상단 구석)
obtn = Button(
    otk, text="click", command=hello
)  # 생성된 윈도우창 객체에 버튼 객체 생성, 버튼의 텍스트 지정, 버튼 클릭시 반응(함수) 지정
obtn.pack()  # 버튼의 위치를 윈도우창에 배치
otk.mainloop()  # 윈도우 창 실행

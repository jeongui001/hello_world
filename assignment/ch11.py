# ch11.py

# 5번 ~ 10번
from tkinter import *

oroot = Tk()
oroot.geometry("400x300")
oroot.title("조각 피자 주문 프로그램")
olabel = Label(oroot, text="피자")
olabel.pack()

pizza = {
    0: "치즈 피자 (3200원)",
    1: "콤비네이션 피자 (3500원)",
    2: "불고기 피자 (3600원)",
}
check_value = {}
for i in range(len(pizza)):
    check_value[i] = BooleanVar()
    ocheckbutton = Checkbutton(oroot, variable=check_value[i], text=pizza[i])
    ocheckbutton.pack(anchor="w")


def buy():
    sum = 0
    olabel2 = Label(oroot, text="주문내역:")
    olabel2.pack()
    for i in check_value:
        if check_value[i].get() == True:
            checked_pizza = pizza[i]
            sum += int(checked_pizza[len(checked_pizza) - 6 : len(checked_pizza) - 2])
            # print(checked_pizza)
            Label(oroot, text="- " + checked_pizza).pack()

    olabel3 = Label(oroot, text="\n총 가격: " + str(sum) + "원")
    olabel3.pack()


obutton = Button(oroot, text="주문", command=buy)
obutton.pack()
oroot.mainloop()

# 프롬프트 "python과 Tkinter로 조각 피자 주문 프로그램을 작성해줘"

import tkinter as tk
from tkinter import messagebox

# 피자 가격 (조각당)
pizza_prices = {
    "치즈 피자": 3000,
    "페퍼로니 피자": 3500,
    "불고기 피자": 4000
}

def order_pizza():
    pizza = pizza_var.get()
    slices = slice_var.get()

    if slices <= 0:
        messagebox.showwarning("경고", "조각 수를 1개 이상 선택하세요.")
        return

    price_per_slice = pizza_prices[pizza]
    total_price = price_per_slice * slices

    result_label.config(
        text=f"주문 내역\n"
             f"- 피자 종류: {pizza}\n"
             f"- 조각 수: {slices}조각\n"
             f"- 총 가격: {total_price:,}원"
    )

# 메인 창
root = tk.Tk()
root.title("🍕 조각 피자 주문 프로그램")
root.geometry("300x350")

# 제목
tk.Label(root, text="조각 피자 주문", font=("Arial", 14, "bold")).pack(pady=10)

# 피자 선택
tk.Label(root, text="피자 종류 선택").pack()
pizza_var = tk.StringVar(value="치즈 피자")

for pizza in pizza_prices.keys():
    tk.Radiobutton(root, text=pizza, variable=pizza_var, value=pizza).pack(anchor="w", padx=50)

# 조각 수 선택
tk.Label(root, text="조각 수 선택").pack(pady=10)
slice_var = tk.IntVar(value=1)
tk.Spinbox(root, from_=1, to=10, textvariable=slice_var, width=5).pack()

# 주문 버튼
tk.Button(root, text="주문하기", command=order_pizza, bg="orange").pack(pady=15)

# 결과 출력
result_label = tk.Label(root, text="", justify="left")
result_label.pack()

root.mainloop()

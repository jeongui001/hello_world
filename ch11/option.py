# option.py

import tkinter as tk

root = tk.Tk()

option_list = ["option1", "option2", "option3"]

selected_option = tk.StringVar()

selected_option.set(option_list[0])  # 기본값 설정

# option_menu = tk.OptionMenu(root, tk.StringVar(), "option1", "option2", "option3")
option_menu = tk.OptionMenu(root, selected_option, *option_list)

option_menu.pack()
root.mainloop()

# 8차시
# def list_max(num_list):
#     max = num_list[0]
#     for num in num_list:
#         if num > max:
#             max = num
#     print(max)


# aa = [1, 2, 3, 4, 5]
# list_max(aa)


# def list_min(num_list):
#     min_value = num_list[0]
#     for num in num_list:
#         if num < min_value:
#             min_value = num
#     print(min_value)


# numbers = [42, 17, 23, 56, 9, 34]
# list_min(numbers)


# 9차시
# class Student:
#     school = "High School"

#     def __init__(self, name, grade):
#         self.name = name
#         self.grade = grade


# s1 = Student("Alice", 1)

# print(Student.school)
# print(s1.school)
# print(s1.name)

# 10차시
# from math import factorial

# print(factorial(5))

# class Animal:
#     def speak(self):
#         return "Animal speaks"

# class Dog(Animal):
#     def speak(self):
#         return "Woof!"

# 11차시
import tkinter as tk
from tkinter import messagebox


def on_buton_click():
    messagebox.showinfo("알림", "버튼이 클릭되었습니다!")


root = tk.Tk()
root.title("간단한 Tkinter 앱")
root.geometry("300x200")

btn = tk.Button(root, text="클릭하세요", command=on_buton_click)
btn.pack(pady=20)

root.mainloop()

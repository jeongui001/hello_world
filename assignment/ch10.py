# ch10.py


# 5번
# class Phone:
#     def __init__(self, phone_number, phone_color):
#         self.number = phone_number
#         self.color = phone_color


# phone = Phone("010-1234-5678", "검정")
# print(phone.number)
# print(phone.color)


# 6,7 번
# class Phone:
#     def __init__(self, phone_number, phone_color):
#         self.number = phone_number
#         self.color = phone_color


# class SmartPhone(Phone):
#     def __init__(self, phone_number, phone_color, phone_company):
#         super().__init__(phone_number, phone_color)
#         self.company = phone_company


# apple = SmartPhone("010-1234-5678", "검정", "애플")
# print(apple.number)
# print(apple.color)
# print(apple.company)


# 8번
# class Phone:
#     def __init__(self, phone_number, phone_color):
#         self.number = phone_number
#         self.color = phone_color

#     def showInfo(self):
#         print(f"전화번호: {self.number}")
#         print(f"색상: {self.color}")


# phone = Phone("010-1234-5678", "검정")
# phone.showInfo()


# 9번
class Phone:
    def __init__(self, phone_number, phone_color):
        self.number = phone_number
        self.color = phone_color

    def showInfo(self):
        print(f"전화번호: {self.number}")
        print(f"색상: {self.color}")


class SmartPhone(Phone):
    def __init__(self, phone_number, phone_color, phone_company="미정"):
        super().__init__(phone_number, phone_color)
        self.company = phone_company


apple = SmartPhone("010-1234-5678", "화이트")
apple.showInfo()


# 10번
# class Phone:
#     def __init__(self, phone_number, phone_color):
#         self.number = phone_number
#         self.color = phone_color

#     def showInfo(self):
#         print(f"전화번호: {self.number}")
#         print(f"색상: {self.color}")


# class SmartPhone(Phone):
#     def __init__(self, phone_number, phone_color, phone_company):
#         super().__init__(phone_number, phone_color)
#         self.company = phone_company

#     def showInfo(self):
#         super().showInfo()
#         print(f"회사: {self.company}")


# apple = SmartPhone("010-1234-5678", "검정", "애플")
# apple.showInfo()

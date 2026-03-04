# ch09.py


# 3번 ~9번
class Phone:
    def __init__(self, maker, model_year, color):
        self.maker = maker
        self.model_year = model_year
        self.color = color
        print("휴대폰 생성")

    def info(self):
        print(f"제조사는 {self.maker}입니다.")
        print(f"출고년도는 {self.model_year}입니다.")
        print(f"색상은 {self.color}입니다.")

    def setInfo(self, maker, model_year, color):
        self.maker = maker
        self.model_year = model_year
        self.color = color


my_phone = Phone("samsung", "2020", "black")
my_phone.info()
my_phone.setInfo("apple", "2025", "gray")
my_phone.info()

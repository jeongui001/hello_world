# human.py


class Human:
    eyes = 2
    nose = 1
    mouth = 1

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"이름 : {self.name}")
        print(f"나이 : {self.age}")

    def eat(self):
        print("먹다")

    def sleep(self):
        print("자다")

    def talk(self):
        print("말하다")


class Student(Human):
    def study(self):
        print("공부하다")


stu1 = Student("학생1", 17)

stu1.introduce()
stu1.sleep()
stu1.study()
print(f"코의 개수 : {stu1.nose}")

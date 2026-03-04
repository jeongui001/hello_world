#2-1
# a = 3.14
# b = True
# c = "False"
# print(type(a))
# print(type(b))
# print(type(c))

#2-2
# first_num = input("두 개의 수를 입력하세요.(첫번째)")
# second_num = input("두 개의 수를 입력하세요.(두번째)")
# first_num = float(first_num)
# second_num = float(second_num)

# add = first_num+second_num
# sub = first_num-second_num
# mul = first_num*second_num
# div = first_num/second_num

# print("사칙연산 결과", "\n더하기 : ", add, "\n빼기 : ", sub, "\n곱하기 : ", mul, "\n나누기 : ", div)

#3-2
# score = input("점수를 정수로 입력하세요")
# score = int(score)

# if score>100 or score<0:
#     print("올바른 점수를 입력하세요")
# elif score>=90:
#     print("A")
# elif 80<=score:
#     print("B")
# elif 70<=score:
#     print("C")
# else:
#     print("F")
# print("if문 종료됨")

#4-1
# fruits = ["banana", "peach", "lemon", "grape"]
# print(fruits[2])

#4-2
student3 = {"나이": 22, "직업": "학생", "취미": "게임"}
student3["도시"] = "수원"
for key in student3.keys():
    print(key)

    
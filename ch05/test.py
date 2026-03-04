# 연습문제 22
# price = 0
# while price != -1:
#     price = int(input("가격"))
#     if price>10000:
#         print('너무 비싸요')
#     elif price>5000:
#         print('괜찮아요')
#     else:
#         print('싸요')

# 연습문제 24
# for i in range(0, 101):
#     if i%3 !=0:
#         continue
#     print(i)

# 연습문제 24
# for i in range(1, 11):
#     if i%3 ==0:
#         continue
#     print(i)

# 연습문제 25
# num = int(input('정수입력'))

# total = 0
# for i in range(num+1):
#     total +=i

# print('총 합은', total, '입니다.')

#연습문제 27
# num = int(input('정수입력'))

# total = 0
# i = 0
# while i<num:
#     i += 1
#     total += i
    

# print('총 합은', total, '입니다.')

#연습문제 28
# num = int(input('정수입력'))

# total = 0
# i = 0
# while True:
#     i += 1
#     total += i 
#     if num == i:
#         break

# print('총 합은', total, '입니다.')

#연습문제 29
# num1 = int(input('첫번째 수를 입력하세요'))
# num2 = int(input('마지막 수를 입력하세요'))

# total = 0
# for i in range(num1, num2+1):
#     total = total + i
# print(total)

# total = 0
# while True:
#     total += num1
#     num1 += 1
#     if num1 == num2+1:
#         break
# print(total)

# #연습문제 30
# num = int(input('수 입력'))
# total = 0
# for i in range(num+1):
#     if i%3 == 0:
#         total += i
# print(total)

# total = 0
# i = 0
# while i < num+1:
#     if i%3 == 0:
#         total += i
#     i += 1
# print(total)

# #연습문제 33
# for i in range(10):
#     mul = 1*(i+1)
#     print(mul)

#연습문제 34 ~ 36
for i in range(1,10):
    print()
    print(i,"단")
    for j in range(1,10):
        mul = j*(i)
        print(mul)
    
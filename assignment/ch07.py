# ch07.py


# 3번
# def calculate_area(length, width=10):
#     return length * width


# print(calculate_area(5))
# print(calculate_area(5, 20))


# # 4번
# def add_numbers(a, b):
#     return a + b


# print(add_numbers(10, 20))  # 30


# 5번
# def inner_function(x, y):
#     return x + y


# def outer_function(x, y):
#     return inner_function(x, y)


# add_10 = outer_function(10, 5)
# print(add_10)


# 6번
# def add_numbers(a, b):
#     result = a + b
#     return result


# result = add_numbers(10, 20)
# print(result)


# 7번
# def message():
#     print("A")
#     print("B")


# message()
# print("C")
# message()

# 8번
# print("A")


# def message():
#     print("B")


# print("C")
# message()


# 9번
# def check_odd_even(num):
#     if num % 2 == 0:
#         return "Even"
#     elif num % 2 == 1:
#         return "Odd"


# print(check_odd_even(-2))  # 출력: Even
# print(check_odd_even(7))  # 출력: Odd


# 10번
# def calculate_average(nums):
#     if len(nums) == 0:
#         return 0
#     return sum(nums) / len(nums)


# num_list = []
# average = calculate_average(num_list)
# print("평균: ", average)

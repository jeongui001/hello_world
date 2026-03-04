# ch08.py

# 1번
# a = [1, 2, 3, 4]
# a[0], a[3] = a[3], a[0]
# print(a)

# 2번
# lst = [40, 20, 30, 10]
# lst[0], lst[3] = lst[3], lst[0]
# print(lst)

# 3번
# arr = [3, 6, 9, 12]
# arr[0], arr[2] = arr[2], arr[0]
# print(arr)

# 4번
# a = [1, 2, 3]
# b = a
# print(id(a) == id(b))

# # 5번
# x = 42
# y = 42
# print(id(x) == id(y))

# 6번
# a = [3, 6, 7, 4, 9, 10, 13]
# for i in range(len(a)):
#     if a[i] % 2 == 0:
#         first_even_order = i
#         break
# for i in range(len(a) - 1, 0 - 1, -1):
#     if a[i] % 2 == 1:
#         last_odd_order = i
#         break

# a[first_even_order], a[last_odd_order] = a[last_odd_order], a[first_even_order]
# print(a)

# 7번
# a = [3, 6, 7, 4, 9, 10, 13, 50, 30, 20]
# max = a[0]
# for i in a:
#     if max < i:
#         max = i
# print(max)


# 9번
# def selection_sort(arr):
#     for i in range(len(arr)):
#         min_idx = i
#         for j in range(i + 1, len(arr)):
#             if arr[j] < arr[min_idx]:
#                 min_idx = j
#         # 빈칸에 들어갈 코드
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]
#     return arr


# data = [64, 25, 12, 22, 11]
# print(selection_sort(data))

# 10번
ex_dict = {"a": 10, "b": 20, "c": 30}
sum = 0
for value in ex_dict.values():
    sum += value
print(sum)

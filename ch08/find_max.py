# case 1
# ca = [10, 17, 13, 11]
# max = ca[0]
# if max < ca[1]:
#     max = ca[1]
# if max < ca[2]:
#     max = ca[2]
# if max < ca[3]:
#     max = ca[4]

# print(max)

# case 2
# ca = [10, 17, 13, 11]
# max = ca[0]
# for i in range(0,4,1):
#     if max < ca[i]:
#         max = ca[i]
# print(max)

# case 3
ca = [10, 17, 13, 11]
max = ca[0]
for i in ca:
    if max < i:
        max = i
print(max)
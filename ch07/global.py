# 페이지 18
# def scope_test():
#     global a
#     a = a+3
#     print("scope 안의 값은", a)

# a = 0
# print("scope 밖의 값은", a)
# scope_test()
# print("scope 호출 후 값은", a)

# 페이지 19
def scope_test(a):
    a = a+3
    print("scope 안의 값은", a)
    return a

a = 0
print("scope 밖의 값은", a)
a = scope_test(a)
print("scope 호출 후 값은", a)
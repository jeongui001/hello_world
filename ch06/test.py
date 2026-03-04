# def fadd(a,b):
#     c = a+b
#     return c

# def fsub(a,b):
#     c = a-b
#     return c

# def fmul(a,b):
#     c = a*b
#     return c

# def fdiv(a,b):
#     c = a/b
#     return c

# def fcal(a,b):
#     c_add = fadd(a,b)
#     c_sub = fsub(a,b)
#     c_mul = fmul(a,b)
#     c_div = fdiv(a,b)
#     return c_add, c_sub, c_mul, c_div

# a,b,c,d = fcal(100,3)
# print(a,b,c,d)
# print(type(b))

##############################

# sta = "python example"

# def string_length(stb):
#     slength = 0
#     for i in stb:
#         slength += 1
#     return(slength)

# lena = string_length(sta)
# print(lena)
# print(len(sta))

#################################

num = int(input("정수 입력, 1~9까지"))

def add_to_100(fnum):
    total = 0
    for i in range(1,101):
        if i%fnum == 0:
            total += i
    return total

total_num = add_to_100(num)
print(total_num)
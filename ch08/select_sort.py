# myway
ca = [21, 10, 15, 11, 13]
# # 1차
# mina = ca[0]
# minix = 0
# for i in range(1,5,1):
#     if mina>ca[i]:
#         mina = ca[i]
#         minix = i

# temp = ca[0]
# ca[0] = mina
# ca[minix] = temp

# # 2차
# mina = ca[1_]
# minix = 1_
# for i in range(2_,5,1):
#     if mina>ca[i]:
#         mina = ca[i]
#         minix = i

# temp = ca[1_]
# ca[1_] = mina
# ca[minix] = temp

# 1~4차
# for j in range(0,4,1):
#     mina = ca[j]
#     minix = j
#     for sb in range(j+1,5,1):
#         if mina>ca[sb]:
#             mina = ca[sb]
#             minix = sb

#     temp = ca[j]
#     ca[j] = mina
#     ca[minix] = temp
# print(ca)

#함수로 만들기
def fselsort(cb : list) -> list:
    cc = cb[:] # 받은 리스트를 수정하지 않겠다.
    n = len(cc)
    for j in range(0,n-1,1):
        mina = cc[j]
        minix = j
        for sb in range(j+1,n,1):
            if mina>cc[sb]:
                mina = cc[sb]
                minix = sb

        temp = cc[j]
        cc[j] = mina
        cc[minix] = temp
    return cc

print(ca) # 선택 정렬 전
print(fselsort(ca)) # 선택 정렬 후
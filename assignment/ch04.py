#1
movie_rank = ["하얼빈", "무파사:라이온킹", "소방관"]

#2
movie_rank.append("위키드")

#3
movie_rank.insert(3,"모아나2")

#4
movie_rank.remove("소방관")

#5
nums = [1,2,3,4,5]
sum_of_nums = sum(nums)
print(sum_of_nums)

#6
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
print(len(cook))

#7
t = 1,2,3,4
print(type(t))

#8
t = ('a', 'b', 'c')
new_t = list(t)
new_t[0] = 'A'
t = tuple(new_t)
print(t)

#9
icecream = {'메로나':1000, '폴라포':1200, '빵빠레':1800}

#10
icecream['죠스바'] = 1200
icecream['월드콘'] = 1500

#11
icecream['메로나'] = 1300
print(icecream)
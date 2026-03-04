# mex1_example3.py
from mex1 import * # import mex1과 다르게 코드 간결화가 가능하다.

value = plus(10, 20)
print(value) # 30

p4 = Cvalue()
print(p4.lista) # []
p4.add("장미")
p4.add("백합")
p4.add("튤립")
p4.fprint() # ['장미', '백합', '튤립']

p1.add(6)
print(p1.lista) # [1, 2, 3, 6]  
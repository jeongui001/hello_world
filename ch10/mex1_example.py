# mex1_example.py

import mex1
import mex1 as m1 # 별칭 사용 가능
# mex1.py 클래스 활용
p2 = mex1.Cvalue()
p2.add(11)
p2.add(21)
p2.add(31)
p2.fprint()

# mex1.py 함수 활용
value = mex1.plus(10,20)
print(value)

# mex1.py 변수 활용
print(mex1.p1) # p1객체의 메모리주소
print(mex1.p1.lista)
mex1.p1.add(4)
mex1.p1.fprint()
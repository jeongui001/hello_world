# mex1_example2.py

from mex1 import plus # [1,2,3] 출력 -> 이 경우도 mex1이 자동 실행됨을 확인

value = plus(10, 20)
print(value) # 30 출력

# 파이썬 모듈 임포트시 from으로 일부만 가져오는 이유
# 1. 코드 간결화(가독성)
# 2. 네임스페이스 충돌 방지
# 3. 기능 사용 명확성
# 단 성능 차이는 거의 없음
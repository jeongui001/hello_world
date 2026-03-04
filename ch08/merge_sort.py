import random
import time

# 1. 두 개의 정렬된 리스트를 하나로 합치는 함수
def merge(left, right):
    result = []
    i = 0  # 왼쪽 리스트용 인덱스
    j = 0  # 오른쪽 리스트용 인덱스

    # 두 리스트에 숫자가 남아있는 동안 비교해서 작은 걸 먼저 넣음
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 한쪽이 먼저 끝나면 남은 숫자들을 뒤에 다 붙임
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# 2. 리스트를 반으로 쪼개는 메인 함수
def fmergesort(cb: list) -> list:
    if len(cb) <= 1:
        return cb  # 데이터가 1개면 정렬할 게 없으니 그대로 반환

    # 반으로 나누기
    mid = len(cb) // 2
    left_side = fmergesort(cb[:mid])  # 왼쪽 덩어리 (재귀)
    right_side = fmergesort(cb[mid:]) # 오른쪽 덩어리 (재귀)

    # 쪼개진 애들을 합쳐서 반환
    return merge(left_side, right_side)

# 선택 정렬
def fselsort(cb : list) -> list:
    cc = cb[:] 
    n = len(cc) # 리스트의 전체 길이를 구함
    
    # 4 대신 (n - 1)을, 5 대신 n을 넣습니다.
    for j in range(0, n - 1, 1):
        mina = cc[j]
        minix = j
        for sb in range(j + 1, n, 1):
            if mina > cc[sb]:
                mina = cc[sb]
                minix = sb

        temp = cc[j]
        cc[j] = mina
        cc[minix] = temp
    return cc

# 테스트용 데이터: 0부터 10,000까지의 숫자를 무작위로 5,000개 생성
data_size = 5000
test_data = [random.randint(0, 10000) for _ in range(data_size)]

# 1. 선택 정렬 속도 측정
sel_data = test_data[:]
start = time.time()
fselsort(sel_data)
print(f"선택 정렬 걸린 시간: {time.time() - start:.4f}초")

# 2. 병합 정렬 속도 측정
merge_data = test_data[:]
start = time.time()
fmergesort(merge_data)
print(f"병합 정렬 걸린 시간: {time.time() - start:.4f}초")

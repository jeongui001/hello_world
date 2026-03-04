# check_box.py

import tkinter

# 1. 메인 윈도우 생성
oroot = tkinter.Tk()
oroot.title("커피 주문 시스템")

# 2. 메뉴 데이터 (딕셔너리)
# 메뉴가 추가되더라도 아래 딕셔너리만 수정하면 됩니다.
# coffee = {0: "아메리카노", 1: "라떼", 2: "카푸치노", 3: "에스프레소"}
coffee = ["아메리카노", "라떼", "카푸치노", "에스프레소"]

# 3. 체크박스의 상태(On/Off)를 저장할 딕셔너리
check_value = {}

# 4. 반복문을 사용하여 체크박스 자동 생성
for i in range(len(coffee)):
    # 각 메뉴별로 BooleanVar(True/False 저장 변수) 생성
    check_value[i] = tkinter.BooleanVar()

    # 체크버튼 위젯 생성 및 배치
    ocheckbutton = tkinter.Checkbutton(oroot, variable=check_value[i], text=coffee[i])
    ocheckbutton.pack(anchor="w")  # 'w'는 West(왼쪽 정렬)를 의미합니다.


# 5. 주문 버튼 클릭 시 실행될 함수
def buy():
    print("--- 주문 내역 ---")
    for i in check_value:
        # 체크박스가 선택되어 있다면 (True라면)
        if check_value[i].get() == True:
            print(coffee[i])  # 딕셔너리에서 해당 번호의 메뉴명 출력


# 6. 주문 버튼 생성
tkinter.Button(oroot, text="주문", command=buy).pack()

# 7. GUI 실행
oroot.mainloop()

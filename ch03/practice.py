real_ID = "id123"
real_passward = "pw123"

ID = input("아이디를 입력하세요")
if ID==real_ID:
    print("ID 일치!")
    passward = input("비밀번호를 입력하세요")
    if passward==real_passward:
        print("로그인 성공!")
    else:
        print("암호 불일치")
else:
    print("존재하지 않는 ID입니다!")
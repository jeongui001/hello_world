score = input("점수를 입력하세요(소수점 불가) ")
score = int(score)
if (0<=score<=100):
    if(score>80):
        print("점수는",score, "점이고 학점은 A입니다.")
    elif(score>60):
        print("점수는",score, "점이고 학점은 B입니다.")
    elif(score>40):
        print("점수는",score, "점이고 학점은 C입니다.")
    elif(score>20):
        print("점수는",score, "점이고 학점은 D입니다.")
    else:
        print("점수는",score, "점이고 학점은 E입니다.")

else:
    print("올바른 성적을 입력하세요")
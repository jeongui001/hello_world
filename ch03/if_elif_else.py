score = input("점수를 정수로 입력하세요")
score = int(score)

if score>990 or score<0:
    print("올바른 점수를 입력하세요")
elif score>=900:
    print("당신의 토익점수는",score,"이며 상위권입니다.")
elif 600<=score<900:
    print("당신의 토익점수는",score,"이며 중상위권입니다.")
elif 300<=score<600:
    print("당신의 토익점수는",score,"이며 중위권입니다.")
else:
    print("당신의 토익점수는",score,"이며 하위권입니다.")
print("if문 종료됨")
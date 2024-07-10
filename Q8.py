

score = int(input("점수를 입력하세요: "))

if 81 <= score <= 100:
    print("A 학점 입니다.")

elif 61 <= score <= 80:
    print("B 학점 입니다.")
elif 41 <= score <= 60:
    print("C 학점 입니다.")
elif 21 <= score <= 40:
    print("D 학점 입니다.")
elif 0 <= score <= 20:
    print("E 학점 입니다.")

else:
    print("0점부터 100점 사이의 점수를 입력하세요.")


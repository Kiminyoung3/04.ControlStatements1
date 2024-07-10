#fruit 딕셔너리
#사용자가 입력한 값이
#딕셔너리 키 값에 포함되어있다면 "정답입니다" 출력
#아닐 경우 "오답입니다" 출력
#딕셔너리는 키 값으로 조회해야함

fruit = {"봄":"딸기", "여름":"토마토", "가을":"사과"}

data_f = input("계절을 입력하세요: ")

if data_f in fruit :
    print("정답입니다.")
    print(fruit[data_f])
else :
    print("오답입니다.")
#Q7
#사용자로부터 임의의 값 입력받기
#해당 수가 5와 10 사이에 있으면 'ok' 출력
#그렇지 않으면 'no' 출력


num_x = int(input("값을 입력해주세요: "))

if 5 < num_x < 10 :
    print("ok")

#방법1
elif num_x <= 5 :
    print("no")
elif num_x >= 10 :
    print("no")

#방법2
#elif num_x <= 5 or num_x>= 10

#방법3
#else
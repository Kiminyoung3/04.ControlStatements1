#조건문
a = 3
b = 3

if a > b :
    print("a는 b보다 큽니다.") #코드블록
    print("연산을 종료합니다.")
elif a == b :
    print("a와 b는 같습니다.")
    print("연산을 종료합니다.")
else :
    print("b는 a보다 큽니다.")
    print("연산을 종료합니다.")

print("-"*30)
print("저는 들여쓰기를 하지 않은 라인입니다.")

print("-"*30)

a = "김인영"
b = "김또또"

if a != b :
    print("두 사람의 이름은 다릅니다.")
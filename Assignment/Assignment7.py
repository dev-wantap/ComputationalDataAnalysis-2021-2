# 컴퓨팅과데이터처리 7주차 과제 
# 2021024202 김관우

while True:
    a = int(input("첫 번째 숫자 입력: "))
    b = int(input("두 번째 숫자 입력: "))
    ch = input("계산할 연산자 입력")

    if ch == "+":
        print("%d + %d = %d 입니다." % (a, b, a + b))
    elif ch == "-":
        print("%d - %d = %d 입니다." % (a, b, a - b))
    elif ch == "*":
        print("%d * %d = %d 입니다." % (a, b, a * b))
    elif ch == "/":
        print("%d / %d = %d 입니다." % (a, b, a / b))
    elif ch == "%":
        print("%d %% %d = %1f 입니다." % (a, b, a % b))
    elif ch == "//":
        print("%d // %d = %d 입니다." % (a, b, a // b))
    elif "**" == ch:
        print("%d ** %d = %d 입니다." % (a, b, a ** b))

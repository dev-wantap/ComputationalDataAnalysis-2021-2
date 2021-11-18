# 컴퓨팅과데이터처리 11주차 과제
# 2021024202 김관우

import random


def get_lotto():
    lst = list()
    for none in range(6):
        lst.append(random.randint(1, 65))
    return lst


while True:
    num = int(input("게임 수: "))
    if num == 0:
        break
    elif num <= 0:
        print("입력이 잘못되었습니다.")
    else:
        for i in range(num):
            print(get_lotto())

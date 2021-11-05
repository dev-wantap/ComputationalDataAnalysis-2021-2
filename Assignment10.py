# 컴퓨팅과데이터처리 10주차 과제
# 2021024202 김관우

### 숫자맞추기 게임 ###

import random


def is_same(target, number):
    if target == number:
        result = "Win"
    elif target > number:
        result = "High"
    else:
        result = "Low"

    return result


print("######  숫자맞추기 게임 ######")

com_number = random.randint(1, 100)
while True:
    user_number = int(input("1~100까지중 숫자 하나 입력"))
    game_result = is_same(com_number, user_number)
    if game_result == "Win":
        print(game_result)
        break
    else:
        print(game_result)

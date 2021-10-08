import random

ans = ("자! 해보세요", "됐네요, 이사람아", "뭐라고? 다시 생각해보세요", "모르니 두려운 것입니다.", "제 정신이 아니군요", "당신이라면 할 수 있어요", "해도 그만 안해도 그만! 아니겠어요", "맞아요. 올바른 선택입니다.")
question = input("고민을 입력하세요: ")
print("고민 중..."*4)
n = random.randint(1,8)

answer = ans[n]
print(answer)
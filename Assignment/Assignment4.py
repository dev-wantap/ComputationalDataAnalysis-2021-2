Math = float(input("수학 : "))
Eng = float(input("영어 : "))

if (Math + Eng) < 110:
    print("불합격 : 총점으로 불합격")
elif Math < 40:
    print("불합격 : 수학점수 미만으로 불합격")
elif Eng < 40:
    print("불합격 : 영어점수 미만으로 불합격")
else:
    print("합격")


# 컴퓨팅과데이터처리 6주차 과제 
# 2021024202 김관우

guguLine = ""

for i in range(2, 10):
    guguLine += f"#  {i}단  # "
print(guguLine)

for i in range(1, 10):
    guguLine = ""
    for j in range (2, 10):
        guguLine += (str(j)+"*"+str(i)+" = %2d  "%(i*j))
    print(guguLine)


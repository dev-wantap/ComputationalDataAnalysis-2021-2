# 컴퓨팅과데이터처리 6주차 과제 
# 2021024202 김관우

for i in range(2, 10):
    print(f"#  {i}단  #", end=" ")
print()
for i in range(1, 10):
    for j in range (2, 10):
        print(str(j)+"*"+str(i)+" = %2d"%(i*j),  end="  ")
    print()


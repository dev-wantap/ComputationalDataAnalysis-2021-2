parking = []
carName = "A"

while(True):
    select = int(input("<1> 자동차 넣기 <2> 자동차 빼기 <3> 끝 : "))
    
    if (select == 1):
        if (len(parking) >= 5):
            print("주차장이 꽉 차서 못 들어감\n")
        else:
            parking.append(carName)
            print("%s자동차 들어감. 주차장 상태 ===> %s\n" %(carName, parking))
            carName = chr(ord(carName) + 1)
    elif (select == 2):
        if (len(parking) <= 0):
            print("자동차 없음")
        else:
            outCar = parking.pop()
            print("%s자동차 나감. 주차장 상태 ===> %s\n" %(outCar, parking))
            carName = chr(ord(carName) - 1)
    elif (select == 3):
        break
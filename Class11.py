def channel(now_channel, num):
    return now_channel + num


def volume(now_volume, num):
    return now_volume + num


now_cha = 5
now_vol = 4

while True:
    task = input("1.채널, 2.음량, 3.종료\n값을 입력하세요 : ")
    if task == '3':
        break
    elif task == '1':
        num = input("변경할 수치 : ")
        now_cha = channel(now_cha, int(num))
        print("현재 채널 :", now_cha)
    elif task == '2':
        num = input("변경할 수치 : ")
        now_vol = volume(now_vol, int(num))
        print("현재 음량 :", now_vol)

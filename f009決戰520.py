#輸入5,2,0分別代表布、剪刀、石頭
while True:
    try:
        a=int(input())
        b=int(input())
        if (a==5 and b==0) or (a==2 and b==5) or (a==0 and b==2):
            print("A win")
        elif (a==0 and b==5) or (a==5 and b==2) or (a==2 and b==0):
            print("B win")
        else:
            print("Draw")
    except:
        break

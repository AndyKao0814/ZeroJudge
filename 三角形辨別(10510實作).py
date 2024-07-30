while True:
    try:
        a,b,c=sorted(list(map(int,input().split())))    #將陣列由小到大排列
        if a+b<=c:
            print(a,b,c,"\nNo")
        elif (a*a)+(b*b)<(c*c):
            print(a,b,c,"\nObtuse")
        elif (a*a)+(b*b)==(c*c):
            print(a,b,c,"\nRight")
        else:
            print(a,b,c,"\nAcute")
    except:
        break

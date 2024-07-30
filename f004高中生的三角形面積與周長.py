while True:
    try:
        a=float(input())
        b=float(input())
        c=float(input())
        s=(a+b+c)/2
        area=(s*(s-a)*(s-b)*(s-c))**0.5           #海龍公式
        print(float(area))
        print(int(a+b+c))
    except:
        break

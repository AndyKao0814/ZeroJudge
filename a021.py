while True:
    try:
        a,s,b=input().split()
        a=int(a)
        b=int(b)
        if s=="+":
            print(a+b)
        elif s=="-":
            print(a-b)
        elif s=="*":
            print(a*b)
        elif s=="/":
            print(a//b)
    except:
        break

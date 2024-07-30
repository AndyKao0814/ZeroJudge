while True:
    try:
        a,b,c=list(map(int,input().split()))
        s=(a+b+c)/2
        price=s*(s-a)*(s-b)*(s-c)
        print(int(price))
    except:
        break

while True:
    try:
        n=list(map(int,input().strip()))
        a=sum(n[1::2])
        b=sum(n[0::2])
        c=abs(b-a)
        print(c)
    except:
        break

    

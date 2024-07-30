while True:
    try:
        a,b,c=map(int,input().split())
        if a==0 and b==0:
            if c==0:
                print("AND\nOR\nXOR")
            elif c==1:
                print("IMPOSSIBLE")
        elif a!=0 and b==0:
            if c==0:
                print("AND")
            elif c==1:
                print("OR\nXOR")
        elif a!=0 and b!=0:
            if c==0:
                print("XOR")
            elif c==1:
                print("AND\nOR")
        elif a==0 and b!=0:
            if c==0:
                print("AND")
            elif c==1:
                print("OR\nXOR")
    except:
        break

while True:
    try:
        n=int(input())
        for i in range(n):
            h1,m1,h2,m2,m3=map(int,input().split())
            if m2>=m1:
                t=(h2-h1)*60+(m2-m1)
            elif m2<m1:
                t=(60-(m1-m2))
            if t>=m3:
                print("Yes")
            else:
                print("No")
    except:
        break

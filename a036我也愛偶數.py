while True:
    try:
        n,m=map(int,input().split())
        ans=0
        for i in range(n,m+1):
            if i%2==0:
                ans+=i
        print(ans)
    except:
        break

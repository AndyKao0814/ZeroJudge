while True:
    try:
        n=int(input())
        f=int((n*(n+1))/2)
        g=int(n*((n+1)*(2*n+4))/12)
        print(f"{f} {g}")
    except:
        break
    

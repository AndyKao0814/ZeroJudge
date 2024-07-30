while True:
    try:
        n=int(input())
        if n>=15:
            print(n-15)
        elif n<15:
            print(n-15+24)
    except:
        break

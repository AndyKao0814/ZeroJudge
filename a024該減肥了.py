while True:
    try:
        n=int(input())
        if n>50:
            print(n-1)
        else:
            print(n)
    except:
        break

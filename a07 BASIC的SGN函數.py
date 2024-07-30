while True:
    try:
        n=int(input())
        if n>0:
            print("1")
        elif n==0:
            print("0")
        elif n<0:
            print("-1")
    except:
        break

while True:
    try:
        N=float(input())
        M=float(input())
        if (N+M)/2>=60:
            print("Yes")
        else:
            print("No")
    except:
        break

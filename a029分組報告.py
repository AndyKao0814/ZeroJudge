while True:
    try:
        n=int(input())
        if n%3==0:
            output=n//3
        elif n%3!=0:
            output=(n//3)+1
        print(output)
    except:
        break

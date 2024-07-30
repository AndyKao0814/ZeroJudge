while True:
    try:
        a,b=map(int,input().split())
        print(10**20*(a+b))
    except EOFError:
        break

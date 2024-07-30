while True:
    try:
        n=int(input())
        for i in range(n):
            x,y=map(int,input().split())
            r=(x+y)**0.5
            yee=100-r*r
            if 0<yee<=30:
                print("sad!")
            elif 30<yee<=60:
                print("hmm~~")
            elif 60<yee<100:
                print("Happyyyummy")
            else:
                print("evil!!")
    except:
        break

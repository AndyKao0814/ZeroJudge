while True:
    try:
        hh,mm=list(map(int,input().split()))
        hh=int(hh)
        mm=int(mm)
        if hh==7 and mm>=30:
            print("At School")
        elif hh==7 and mm<30:
            print("Off School")
        elif hh<7 and mm>=0 and mm<=59:
            print("Off School")
        elif hh>7 and hh<17 and mm>=0 and mm<=59:
            print("At School")
        elif hh>=17 and mm>=0 and mm<=59:
            print("Off School")
    except:
        break

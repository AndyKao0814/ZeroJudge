while True:
    try:
        time=int(input())
        if time<=25:
            print(25-time)
        elif time>25:
            print(85-time)
    except:
        break

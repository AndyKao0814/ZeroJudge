while True:
    try:
        i=int(input())
        if i%2==0:
            print("Even")
        elif i%2!=0:
            print("Odd")
    except EOFError:
        break
    except ValueError:
        break

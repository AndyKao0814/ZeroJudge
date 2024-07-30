while True:
    try:
        n=input()
        print("hello,",n)
    except EOFError:
        break
    except ValueError:
        break

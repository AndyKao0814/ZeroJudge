while True:
    try:
        F=int(input())
        C=(F-32)*(5/9)
        print('%.3f'%C)
    except EOFError:
        break
    except ValueError:
        break

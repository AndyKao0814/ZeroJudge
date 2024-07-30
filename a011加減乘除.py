while True:
    try:
        output=0
        a,s,b=input().split(' ')
        a=int(a)
        b=int(b)
        if(s=='+'):
            output=a+b
        elif(s=='-'):
            output=a-b
        elif(s=='*'):
            output=a*b
        else:
            output=a/b
        print(int(output))
    except EOFError:
        break
    except ValueError:
        break

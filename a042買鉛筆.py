while True:
    try:
        n=int(input())
        output=50*(n//12)+5*(n%12)
        print(output)
    except:
        break

while True:
    try:
        age=int(input())
        if age<=5:
            print("0")
        elif age>=6 and age<=11:
            print("590")
        elif age>=12 and age<=17:
            print("790")
        elif age>=18 and age<=59:
            print("890")
        else:
            print("399")
    except:
        break

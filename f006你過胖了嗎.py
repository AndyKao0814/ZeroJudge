while True:
    try:
        h=float(input())
        w=float(input())
        h=h/100
        BMI=w/(h**2)
        if BMI<18.5:
            print("過輕")
        elif BMI>=18.5 and BMI<24:
            print("健康")
        elif BMI>=24 and BMI<27:
            print("過重")
        else:
            print("肥胖")
    except:
        break

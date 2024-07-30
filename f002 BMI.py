while True:
    try:
        h=float(input())
        m=float(input())
        h=h/100
        BMI=m/(h**2)
        print(float(BMI))
    except EOFError:
        break
    except ValueError:
        break

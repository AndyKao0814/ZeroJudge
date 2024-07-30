import math

while True:
    try:
        n = int(input())
        if n <= 1:
            print("非質數")
        elif n <= 3:
            print("質數")
        elif n % 2 == 0 or n % 3 == 0:
            print("非質數")
        else:
            is_prime = True
            i = 5
            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    print("非質數")
                    is_prime = False
                    break
                i += 6
            if is_prime:
                print("質數")
    except:
        break

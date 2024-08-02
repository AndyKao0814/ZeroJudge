n = int(input())
_ = input() #第一列以及其它測試資料間有一空白行
 
for _ in range(n):
    A = int(input())
    F = int(input())
    for i in range(F):
        for j in range(A+1):
            for k in range(j):
                print(j, end="")
            print()
 
        for j in range(A-1, 0, -1):
            for k in range(1, j+1):
                print(j, end="")
            print()
 
        print()

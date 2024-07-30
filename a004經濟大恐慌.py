while True:
    try:
        n=int(input())
        m=list(map(int,input().split()))
        price=0
        s=0
        for i in range(n):
            price+=1
            s+=int(m[i]*price)           # 將output的數值加上每個項目 ( 使用 int 將項目轉換成數字 )
        print(s)
    except EOFError:
        break
    except ValueError:
        break

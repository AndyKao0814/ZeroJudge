# 無限循環，直到遇到異常
while True:
    try:
        # 讀取輸入並將其拆分為三個整數 a, b, c
        a, b, c = map(int, input().split()) 
        
        # 檢查 a 和 b 是否都為 0
        if a == 0 and b == 0:
            if c == 0:
                # 當 a, b, c 均為 0 時，打印 AND, OR, XOR
                print("AND\nOR\nXOR")
            elif c == 1:
                # 當 a 和 b 均為 0 且 c 為 1 時，打印 IMPOSSIBLE
                print("IMPOSSIBLE")
        
        # 檢查 a 不為 0 且 b 為 0
        elif a != 0 and b == 0:
            if c == 0:
                # 當 a 不為 0，b 為 0 且 c 為 0 時，打印 AND
                print("AND")
            elif c == 1:
                # 當 a 不為 0，b 為 0 且 c 為 1 時，打印 OR 和 XOR
                print("OR\nXOR")
        
        # 檢查 a 和 b 均不為 0
        elif a != 0 and b != 0:
            if c == 0:
                # 當 a 和 b 均不為 0 且 c 為 0 時，打印 XOR
                print("XOR")
            elif c == 1:
                # 當 a 和 b 均不為 0 且 c 為 1 時，打印 AND 和 OR
                print("AND\nOR")
        
        # 檢查 a 為 0 且 b 不為 0
        elif a == 0 and b != 0:
            if c == 0:
                # 當 a 為 0，b 不為 0 且 c 為 0 時，打印 AND
                print("AND")
            elif c == 1:
                # 當 a 為 0，b 不為 0 且 c 為 1 時，打印 OR 和 XOR
                print("OR\nXOR")
    except:
        # 當遇到異常時，退出循環
        break

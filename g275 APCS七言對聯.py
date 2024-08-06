while True:  # 無限迴圈，直到發生異常（如EOFError）時才會退出
    try:
        n = int(input())  # 輸入一個正整數，代表對聯數量
        for _ in range(n * 2):  # 遍歷 n*2 次，因為每次要讀取兩行輸入
            # 讀取第一行的7個整數
            a, b, c, d, e, f, g = map(int, input().split())
            # 讀取第二行的7個整數
            h, i, j, k, l, m, n = map(int, input().split())

            # 初始化一個空的結果列表
            results = []

            # 檢查每個條件，並將結果添加到 results 列表中
            if (b == d or i == k or b != f or i != m):
                results.append("A")
            if (g == 0 or n == 1):
                results.append("B")
            if (b == i or d == k or f == m):
                results.append("C")
            if not results:  # 如果沒有任何條件匹配，添加 "None"
                results.append("None")

            # 將所有匹配的結果拼接成一個字串，並打印出來
            print(''.join(results))
    except:  # 當發生任何異常時（如EOFError），跳出迴圈
        break

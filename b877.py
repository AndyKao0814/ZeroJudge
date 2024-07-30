# 讀取輸入
a, b = map(int, input().split())

# 計算從a到b的下一個頻道的次數
if b >= a:
    steps = b - a
else:
    steps = (b + 100) - a

# 輸出結果
print(steps)

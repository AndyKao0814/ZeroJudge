T = int(input())  # 讀取測試資料的組數
results = []  # 用來儲存結果

for _ in range(T):
    n = input().strip()  # 讀取一組測試資料
    result = 1
    for i in range(len(n) - 1):
        result *= int(n[i]) * int(n[i + 1])
    results.append(result)

for res in results:
    print(res)

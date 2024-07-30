# 讀取輸入的數量 n
n = int(input())
for i in range(n):
    # 讀取每一對 m 和 p 的值
    m, p = map(int, input().split())
    # 計算變化百分比
    x = ((p - m) / m) * 100
    # 若 x 小於 0，調整 x 以確保正確的格式
    if x < 0:
        x = x - 0.000001
    # 若 x 大於 0，調整 x 以確保正確的格式
    elif x > 0:
        x = x + 0.000001
    # 根據條件判斷輸出 "dispose" 或 "keep"
    if x >= 10 or x <= -7:
        print(f"{x:.2f}% dispose")
    else:
        print(f"{x:.2f}% keep")


#這題要注意誤差值
#若 x < 0 將 x+0.000001 確保output不會出現微小誤差
#反之，若 x > 0 將 x-0.000001 確保output不會出現微小誤差
#最後再用格式化字串輸出結果 注意空格

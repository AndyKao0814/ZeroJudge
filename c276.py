# 讀取輸入數據
secret = input().strip()
n = int(input().strip())
guesses = [input().strip() for _ in range(n)]

# 定義一個函數來計算 xAyB 的結果
def calculate_hints(secret, guess):
    A = sum(1 for s, g in zip(secret, guess) if s == g)
    B = sum(1 for g in guess if g in secret) - A
    return f"{A}A{B}B"

# 對每個猜測計算並輸出結果
for guess in guesses:
    result = calculate_hints(secret, guess)
    print(result)

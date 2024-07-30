def get_feedback(secret, guess):
    # 初始化計數變量
    A = 0
    B = 0
    
    # 將秘密數字和猜測數字轉換為字串以便逐位比較
    secret = str(secret)
    guess = str(guess)
    
    # 創建列表標記哪些數字已經被計數
    secret_counted = [False] * 4
    guess_counted = [False] * 4
    
    # 第一次遍歷：計數 'A' (位置和數字都正確)
    for i in range(4):
        if guess[i] == secret[i]:
            A += 1
            secret_counted[i] = True
            guess_counted[i] = True
    
    # 第二次遍歷：計數 'B' (數字正確但位置不對)
    for i in range(4):
        if not guess_counted[i]:  # 跳過已經計數的數字
            for j in range(4):
                if not secret_counted[j] and guess[i] == secret[j]:
                    B += 1
                    secret_counted[j] = True
                    break
    
    # 返回結果字串，格式為 xAyB
    return f"{A}A{B}B"

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    # 讀取秘密數字和猜測次數
    secret = data[0]
    n = int(data[1])
    
    # 處理每一個猜測
    guesses = data[2:2+n]
    for guess in guesses:
        result = get_feedback(secret, guess)
        print(result)

if __name__ == "__main__":
    main()

import math    #匯入內建的math mod

while True:
    try:
        n = input()  # 讀取用戶輸入的字符串
        n = n.split()  # 將字符串分割成列表，預期列表有兩個元素
        ans = 1  # 初始化結果為 1
        n1 = int(n[0])  # 將列表的第一個元素轉換為整數 n1
        n2 = int(n[1])  # 將列表的第二個元素轉換為整數 n2

        # 如果 n2 大於 n1 - n2，則用 n1 - n2 替換 n2
        if n1 - n2 > n2:
            n2 = n1 - n2

        n3 = n1 - n2  # 計算 n1 - n2

        # 計算 C(n1, n2) 的對數值
        for i in range(n2 + 1, n1 + 1):
            ans = ans + math.log10(i) - math.log10(n3)  # 使用對數來避免計算大數
            n3 -= 1  # 更新 n3

        print(int(ans))  # 打印結果（組合數的位數）
    except:
        break  # 偵測所有異常並退出循環


#這題用Cn取k的公式會TLE，因為遇到大數時複雜度太大，導致程式效率不佳

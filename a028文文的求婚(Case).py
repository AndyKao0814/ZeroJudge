count = 1  # 初始化計數器

while True:
    try:
        # 讀取年份數量
        m = int(input().strip())
        
        for _ in range(m):
            # 讀取年份
            n = int(input().strip())
            
            # 判斷是否為閏年
            if n % 400 == 0 or (n % 4 == 0 and n % 100 != 0):
                print(f"Case {count}: a leap year")
            else:
                print(f"Case {count}: a normal year")
            
            # 增加計數器
            count += 1
    except EOFError:
        break

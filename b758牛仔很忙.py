import datetime

# 讀取輸入並將其轉換為整數列表
n = [int(i) for i in input().split()]

# 將小時數加上2，分鐘數加上30
n[0], n[1] = n[0] + 2, n[1] + 30

# 創建一個表示時間差的 timedelta 對象
t1 = datetime.timedelta(hours=n[0], minutes=n[1])

# 將 timedelta 對象轉換為字串
t2 = str(t1)

# 如果小時數大於等於23
if n[0] >= 23:
    # 拆分字串以獲取時間部分
    t3 = t2.split()
    t3 = t3[2].split(':')
    # 如果小時數只有一位數，則在前面補0
    if len(t3[0]) == 1:
        t3[0] = '0' + t3[0]
    # 輸出時間的前兩部分（小時和分鐘）
    print(':'.join(t3[:2]))
else:
    # 拆分字串以獲取時間部分
    t3 = t2.split(':')
    # 如果小時數只有一位數，則在前面補0
    if len(t3[0]) == 1:
        t3[0] = '0' + t3[0]
    # 輸出時間的前兩部分（小時和分鐘）
    print(':'.join(t3[:2]))

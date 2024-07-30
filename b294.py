while True:
  try:
    day = int(input())      # 後面完全用不到的數字 ( 但是因為題目有，所以必須要使用 )
    n = [int(i) for i in input().split()]   # 將每天的饅頭數量拆成串列
    total = 0     # 總要要多少錢，預設 0
    price = 1     # 最開始的價格為 1 元
    for i in n:
      total = total + price*i    # 總價增加 price 乘以每天的饅頭數
      price += 1          # 第二天價格就會增加 1
    print(total)                 # 印出總價
  except:
    break

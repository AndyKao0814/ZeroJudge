while True:
  try:
    a, b = map(int, input().split())
    a = a + 2            # 避免 a 為 0 時不好判斷，先將數值加 2
    b = b + 2            # 因為 a 加 2，所以讓 b 也一起加 2
    # 上方三行程式，可使用一行匿名函式 lambda 代替
    # a, b = map(lambda x: int(x)+2, input().split())
    c = 1 - a%2          # 如果 a 為奇數，不需要加上自己 ( 1 - a%2 會等於 0 )
    d = 1 - b%2          # 如果 b 為奇數，不需要加上自己 ( 1 - b%2 會等於 0 )
    r = (b-a+c)//2 + d   # 計算最後結果
    print(r)
  except:
    break

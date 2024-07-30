a = [1]               # 串列第一項為 1
for i in range(1,501):
  a.append(a[i-1]+i)  # 將串列加入 2～500 項目，每個項目的內容為 a[i-1]+i
while True:
  try:
    n = int(input())  # 取得第幾項
    print(a[n-1])     # 印出該項目結果
  except:
    break

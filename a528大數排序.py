while True:  # 無窮迴圈，直到發生異常
    try:
        n = int(input())  # 讀取使用者輸入的整數 n
        list1 = []  # 初始化一個空列表，用於儲存接下來的整數

        for i in range(n):  # 循環 n 次
            list1.append(int(input()))  # 讀取每個整數並添加到列表 list1 中
        
        list1.sort()  # 對列表 list1 進行排序
        
        for i in list1:  # 遍歷排序後的列表
            print(i)  # 打印列表中的每個整數
    
    except:  # 捕捉所有異常
        break  # 如果發生異常，退出迴圈

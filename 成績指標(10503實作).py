while True:
    try:
        # 讀取輸入人数
        n = int(input())
        
        # 讀取分數并排序
        scores = sorted(list(map(int, input().split())))
        
        # 打印所有分數，由小到大
        print(" ".join(map(str, scores)))
        
        # 找出最高的不及格分數和最低的及格分數
        max_fail = -1
        min_pass = 101
        all_pass = True
        all_fail = True
        
        for score in scores:
            if score < 60:
                max_fail = max(max_fail, score)
                all_pass = False
            else:
                min_pass = min(min_pass, score)
                all_fail = False
        
        if all_pass:
            print("best case")
        else:
            print(max_fail)
        
        if all_fail:
            print("worst case")
        else:
            print(min_pass)
    
    except EOFError:
        break

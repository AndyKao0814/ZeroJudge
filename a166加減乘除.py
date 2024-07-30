while True:
    try:
        # 提示用户输入一个算式
        ex = input()
        
        # 计算并输出结果
        result = eval(ex)
        print(result)
    except Exception as e:
        break

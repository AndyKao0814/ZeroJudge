while True:
    try:
        r = float(input()) #float為浮點數
        R = (r*9)/5 + 32 #公式題目有給
        print('%g'%(R)) #%g如果小數點為0，則不會輸出
    except:
        break
#while True: 
    #try:
    #except:
        #break
#多行測資

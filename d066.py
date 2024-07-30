h, m = map(int, input().split(' '))
if 7 <= h <= 16:
    if h == 7 and m < 30:
        print('Off School')
    else:
        print('At School')
else:
    print('Off School')

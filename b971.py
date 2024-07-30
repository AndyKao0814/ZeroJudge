a, b, c = map(int, input().split())

if a < b:
    for i in range(a, b + 1, c):
        print(i, end=" ")

elif a > b:
    for i in range(a, b - 1, -c):
        print(i, end=" ")

else:
    print(a)



n=list(map(int,input().strip()))
a=0
b=0
for i,x in enumerate(n):
    if i%2==0:
        a+=x
    else:
        b+=x
print(abs(a-b))



s=[]
n=int(input())
for i in range(n):
    a=list(map(int,input().split()))
    s.append(a)
s.sort()
for i in range(n):
    print(s[i][0],s[i][1])

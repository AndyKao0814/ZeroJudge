n=int(input())
passcode=input()
for i in range(0,n**2,n+1):
    print(passcode[i],end="")

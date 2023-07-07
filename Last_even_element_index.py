n=int(input())
a=list(map(int,input().split()))
s=0
for i in range(len(a)-1,-1,-1):
    if a[i]%2==0:
        s+=i
        print(i)
        break
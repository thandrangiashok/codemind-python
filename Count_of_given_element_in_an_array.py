n=int(input())
a=list(map(int,input().split()))
p=int(input())
s=0
for i in range(n):
    if p==a[i]:
        s+=1
print(s)
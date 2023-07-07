n=int(input())
a=list(map(int,input().split()))
s=0
for i in range(n):
    s+=a[i]
    t=s/n
print('{:.2f}'.format(t))
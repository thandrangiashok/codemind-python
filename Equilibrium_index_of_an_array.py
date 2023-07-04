t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    for i in range(n):
        l=r=0
        for j in range(i):
            l+=a[j]
        for k in range(i+1,n):
            r+=a[k]
        if l==r:
            print(i)
            break
    else:
        print('-1')
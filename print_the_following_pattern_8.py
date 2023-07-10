n=int(input())
for i in range(n):
    for p in range(1,n-1):
        print(p,end='')
    for j in range(n-3,0,-1):
        print(j,end='')
    print()
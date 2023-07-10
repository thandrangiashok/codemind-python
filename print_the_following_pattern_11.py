n=int(input())
for i in range(1,n+1):
    for p in range(65,65+n):
        print(chr(i+64),end=' ')
    print()
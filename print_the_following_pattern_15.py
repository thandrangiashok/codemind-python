n=int(input())
for i in range(n,0,-1):
    for p in range(65,65+i):
        print(chr(i+64),end=' ')
    print()
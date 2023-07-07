n=int(input())
a=list(map(int,input().split()))
s=int(input())
for i in range(n):
    if a[i]==s:
        print(True)
        break
else:
    print(False)
    
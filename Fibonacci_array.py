n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(n-3):
    if l[i]+l[i+1]==l[i+2]:
        c+=1
if c==n-3:
    print("yes")
else:
    print("no")
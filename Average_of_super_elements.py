a=int(input())
b=list(map(int,input().split()))
c=[]
e=0
for i in b:
    if(i==b.count(i)):
        c.append(i)
        e=1
if(e==1):
    d=set(c)
    e=sum(d)/len(d)
    print("{:.2f}".format(e))
else:
    print(-1)
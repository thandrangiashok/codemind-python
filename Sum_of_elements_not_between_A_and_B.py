n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
ls=[]
for i in range(n):
    if l[i]<a or l[i]>b:
        ls.append(l[i])
print(sum(ls))
n=int(input())
a=list(map(int,input().split()))
s=set(a)
s=list(s)
cnt=0
for i in s:
    if a.count(i)>cnt:
        cnt=a.count(i)
        nu=i
print(nu)
    
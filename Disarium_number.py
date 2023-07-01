n=int(input())
temp=n
sum=0
s=str(n)
l=len(s)
while n>0 and l>=1:
    r=n%10
    sum+=r**l
    n=n//10
    l-=1
if sum==temp:
    print(True)
else:
    print(False)

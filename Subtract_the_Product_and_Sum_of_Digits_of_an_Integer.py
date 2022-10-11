n=int(input())
p=1
s=se=0
while n>0:
    r=n%10
    s+=r
    p*=r
    n=n//10
se=p-s
print(se)
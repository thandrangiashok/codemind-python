n=int(input())
p=1
s=0
while n>0:
    r=n%10
    s+=r
    p*=r
    n=n//10
if p==s:
    print("Spy Number")
else:
    print("Not Spy Number")
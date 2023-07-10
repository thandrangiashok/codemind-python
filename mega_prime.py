def p(n):
    pr=True
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            pr=False
    return pr
n=int(input())
if p(n)==True:
    c=0
    d=0
    while n>0:
        r=n%10
        c+=1
        if p(r)==True:
            d+=1
        n=n//10
    if c==d:
        print("Mega Prime")
    else:
        print("Not Mega Prime")
else:
    print("Not Mega Prime")
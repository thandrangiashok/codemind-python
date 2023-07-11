def prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    else:
        return True
a=int(input())
c=a
a=a+1
b=a
while(True):
    if prime(a):
        break
    a+=1
while(True):
    if prime(b):
        break
    b-=1
print(min(abs(a-c),abs(b-c)))
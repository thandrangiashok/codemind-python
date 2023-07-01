def prime(n):
    is_prime=True
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    if is_prime==True:
        return True
    else:
        return False
a=int(input())
b=int(input())
cnt=0
for i in range(a,b+1):
    if prime(i)==True:
        cnt+=1
print(cnt)
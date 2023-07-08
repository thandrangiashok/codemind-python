def prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
n=int(input())
l=str(n)
s=l[::-1]
s=int(s)
if prime(n)==True and prime(s)==True:
    print('circular prime')
elif prime(n)==True:
    print('prime but not a circular prime')
else:
    print('not prime')
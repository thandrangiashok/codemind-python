def is_prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
d=int(input())
m=int(input())
pc=0
for i in range(d,m+1):
    if is_prime(i)==True:
        pc+=1
print(pc)
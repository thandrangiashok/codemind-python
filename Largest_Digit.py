n=int(input())
p=0
while n>0:
    r=n%10
    if r>p:
        p=r
    n=n//10
print(p)
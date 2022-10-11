n=int(input())
p=e=o=0
while n>0:
    r=n%10
    p+=1
    if r%2==0:
        e+=1
    else:
        o+=1
    n=n//10
if p==e:
    print("Even")
elif p==o:
    print("Odd")
else:
    print("Mixed")
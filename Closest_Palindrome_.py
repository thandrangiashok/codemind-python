def is_palin(n):
    ns=str(n)
    ns=ns[::-1]
    ns=int(ns)
    if n==ns:
        return True
    else:
        return False
n=int(input())
t=n
temp=n
while True:
    n+=1
    if is_palin(n)==True:
        next=n
        break
while True:
    t-=1
    if is_palin(t)==True:
        prev=t
        break
if abs(temp-next)<abs(temp-prev):
    print(next)
elif abs(temp-next)>abs(temp-prev):
    print(prev)
elif abs(temp-next)==abs(temp-prev):
    print(prev,next)
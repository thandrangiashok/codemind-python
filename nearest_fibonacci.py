def fibs(n):
    if n==0:
        print(0)
        return
    f=0
    s=1
    t=f+s
    while t<=n:
        f=s
        s=t
        t=f+s
    if abs(t-n)>abs(s-n):
        print(s)
    elif abs(t-n)==abs(s-n):
        print(s,t)
    else:
        print(t)
n=int(input())
fibs(n)
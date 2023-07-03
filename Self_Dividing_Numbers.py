a=int(input())
b=int(input())
for i in range(a,b+1):
    temp=i
    while i>0:
        r=i%10
        c=0
        if r==0:
            c+=1
            break
        elif temp%r!=0:
            c+=1
            break
        i=i//10
    if c==0:
        print(temp,end=' ')
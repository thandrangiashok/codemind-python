a=input()
a=a.split()
for i in a:
    b=[]
    for j in i:
        b.append(ord(j))
    c=min(b)
    d=max(b)
    print(d-c,end=' ')
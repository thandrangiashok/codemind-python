a=input()
a=a.split()
b=0
c=0
for i in a:
    d=[]
    for j in i:
        d.append(ord(j))
    e=min(d)
    b+=e
    f=max(d)
    c+=f
print(c-b)
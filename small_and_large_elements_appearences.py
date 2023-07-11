a=input()
b=[]
for i in a:
    if i!=' ':
        b.append(ord(i))
c=min(b)
d=max(b)
e=chr(c)
f=chr(d)
print(e,a.count(e),f,a.count(f))
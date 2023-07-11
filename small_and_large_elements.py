a=input()
a=a.split()
c=[]
d=[]
for i in a[0]:
    c.append(ord(i))
for i in a[-1]:
    d.append(ord(i))
print(chr(min(c)),chr(max(d)))
    
    
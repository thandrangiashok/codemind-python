a=input()
a=a.split()
for i in a:
    b=[]
    for j in i:
        b.append(ord(j))
    print(chr(min(b)),chr(max(b)),end=' ')
a=input()
b=0
for i in a:
    if (ord(i)>=123 and ord(i)<=126) or (ord(i)>=91 and ord(i)<=96) or (ord(i)>=58 and ord(i)<=64) or (ord(i)>=33 and ord(i)<=47):
        b+=1
print(b)
a=int(input())
b=int(input())
s=s1=0
for i in range(1,a//2+1):
    if a%i==0:
        s+=i
for j in range(1,b//2+1):
    if b%j==0:
        s1+=j
if a==s1 and b==s:
    print('Amicable')
else:
    print('Not Amicable')
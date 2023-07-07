def is_ugly(num):
    if num<=0:
        return False
    for prime in [2,3,5]:
        while num%prime==0:
            num/=prime
    return num==1
num=int(input())
if is_ugly(num):
    print('Ugly Number')
else:
    print('Not Ugly Number')
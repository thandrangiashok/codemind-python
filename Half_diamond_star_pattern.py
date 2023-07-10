n=int(input())
if n<3:
    print('The pattern is not possible')
else:
    for i in range(1,n):
        print(i*'*')
    for i in range(n,0,-1):
        print(i*'*')
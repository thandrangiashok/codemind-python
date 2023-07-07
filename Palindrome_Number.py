n=int(input())
for i in range(n):
    t=input()
    r=t[::-1]
    if r==t:
        print(True)
    else:
        print(False)
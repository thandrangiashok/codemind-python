a,b=map(int,input().split())
mx=max(a,b)
while True:
    if mx%a==0 and mx%b==0:
        print(mx)
        break
    mx+=1
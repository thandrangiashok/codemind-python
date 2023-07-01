n=int(input())
lst=[0,1]
for i in range(2,n):
    sum=lst[i-1]+lst[i-2]
    lst.append(sum)
for i in range(0,n):
    print(lst[i],end=' ')
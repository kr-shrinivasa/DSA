from collections import Counter
n=int(input())
arr=[]
for i in range(n):
    arr.append(input())

d=Counter(arr[0])
for i in range(1,n):
    comp=Counter(arr[i])
    for i in d:
        if comp[i]==0:
            d[i]=-1
        else:
            d[i]=min(d[i],comp[i])
for i in sorted(d.keys()):
    if d[i]!=-1:
        print(i,d[i])
    
from collections import Counter
arr=list(map(int,input().split()))
d=Counter(arr)
c=0
for i in d:
    if d[i]>2:
        c+=(d[i]*d[i]-1)//2
print(c)

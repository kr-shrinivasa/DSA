# your code goes here
from collections import Counter
n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
    
    
if n==0:
    print(-1)
else:   
    d=Counter(arr)
    m=max(d.values())

    for i in d:
        if d[i]==m:
            print(i)
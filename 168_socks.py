from collections import Counter
n=int(input())
arr=list(map(int,input().split()))
d=Counter(arr)
c=0
for i in d:
    c+=d[i]//2
print(c)
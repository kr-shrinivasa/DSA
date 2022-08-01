from collections import Counter
n=int(input())
s=input()
arr=list(input().split())
d1=Counter(s)
d2=Counter(arr)

l=True
for i in d1:
    if i not in d2:
        l=False
        break
print(l)
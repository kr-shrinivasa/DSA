from collections import Counter
n=int(input())
arr=list(input().split())
for i in range(len(arr)):
    arr[i]=str("".join(sorted(arr[i])))
print(arr)
d=Counter(arr)
print(max(d.values()))

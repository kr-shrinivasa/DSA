from collections import Counter
def smally(n,arr):
    d=Counter(arr)
    s=0
    print(sorted(d.keys()))
    for i in sorted(d.keys()):
        print(d[i])
        d[i],s=s,s+d[i]
    for i in arr:
        print(d[i])

n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
smally(n,arr)

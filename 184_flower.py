from collections import Counter
n=int(input())
arr=list(map(int,input().split()))
# arr.sort()
# print(*arr)
d=Counter(arr)
for i in range(n):
    if i<d[1]:
        arr[i]=1
    elif i<(d[1]+d[2]):
        arr[i]=2
    elif i<(d[1]+d[2]+d[3]):
        arr[i]=3
    elif i<(d[1]+d[2]+d[3]+d[4]):
        arr[i]=4
    else:
        arr[i]=5
    

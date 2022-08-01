n=int(input())
for i in range(n):
    arr=list(map(int,input().split()))
    arr.sort()
    s=sum(arr)
    a=[arr[-1]]
    for i in range(len(arr)-2,-1,-1):
        b=sum(a)
        if s-b==b:
            break
        else:
            a.insert(0,arr[i])
    print(*a)



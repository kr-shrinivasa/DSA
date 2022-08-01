def sel(n,arr):
    l=[1]*n
    r=[1]*n
    for i in range(1,n):
        l[i]=arr[i-1]*l[i-1]
    for i in range(n-2,-1,-1):
        r[i]=arr[i+1]*r[i+1]
    
    for i in range(n):
        print(l[i]*r[i],end=" ")


for i in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    sel(n,arr)
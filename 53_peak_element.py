def peak(n,arr):
    if n==1:
        return 1

    if arr[0]>arr[1]:
        return 1
    for i in range(1,n-1):
        
        if arr[i]>arr[i+1] and arr[i]>arr[i-1]:
            return i+1
        
    if arr[-1]>arr[-2]:
        return n
    return -1






for i in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    print(peak(n,arr))

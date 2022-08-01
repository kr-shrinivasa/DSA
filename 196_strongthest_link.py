def strong(arr,n):
    maxim=float("-inf")
    maxnow=0
    s=0
    start=-1
    end=-1
    for i in range(n):
        maxnow+=arr[i]
        if maxnow>maxim:
            maxim=maxnow
            start=s
            end=i
        if maxnow<0:
            maxnow=0
            s=i+1
    return[start,end,maxim]
n=int(input())
arr=list(map(int,input().split()))
print(*strong(arr,n))
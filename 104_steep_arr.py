n=int(input())
arr=list(map(int,input().split()))
s=0
m=arr[-1]
for i in range(n-1,-1,-1):
    if arr[i]>m:
        m=arr[i]
    elif m>arr[i]:
        s+=m-arr[i]
print(s)

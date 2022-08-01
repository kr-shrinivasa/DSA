n,k=map(int,input().split())
arr=list(map(int,input().split()))
arr[k-1],arr[n-k]=arr[n-k],arr[k-1]
print(*arr)
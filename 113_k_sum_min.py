n,k=map(int,input().split())
arr=list(map(int,input().split()))
maxi=0
mini=1000000
for i in range(n-k+1):
    s=sum(arr[i:i+k])
    
    maxi=max(maxi,s)
    mini=min(mini,s)
print(maxi,mini)

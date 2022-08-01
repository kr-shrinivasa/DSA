n,k=map(int,input().split())
arr=list(map(int,input().split()))
d={}
cs=0
d[cs]=0
lon=-1
for i in range(n):
    cs+=arr[i]
    if cs-k in d:
        lon=max(lon,i-d[cs-k])
    if cs not in d:
        d[cs]=i
print(lon)
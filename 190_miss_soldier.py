n=int(input())
arr=[]
for i in range(n):
    x,y,w=map(int,input().split())
    s=x
    e=x+w
    arr.append([s,e])
arr.sort(key=lambda x:x[0])

m=arr[0][1]
res=0
res+=arr[0][1]-arr[0][0]+1
for i in range(1,n):
    if arr[i][1]<=m:
        continue
    if arr[i][0]<=m:
        res+=arr[i][1]-m
    else:
        res+=arr[i][1]-arr[i][0]+1
    m=arr[i][1]
print(res)


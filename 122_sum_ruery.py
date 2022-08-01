
n,k=map(int,input().split())

arr=list(map(int,input().split()))
csum=[arr[0]]
for i in range(1,n):
    csum.append(arr[i]+csum[-1])


for i in range(k):
    l,r=map(int,input().split())
    l,r=l-1,r-1
    if l-1>=0:
        print(csum[r]-csum[l-1])
    else:
        print(csum[r])
    


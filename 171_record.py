n=int(input())
arr=list(map(int,input().split()))
maxi=arr[0]
maxc=0
mini=arr[0]
minc=0
for i in range(1,n):
    if arr[i]>maxi:
        maxi=arr[i]
        maxc+=1
    if arr[i]<mini:
        mini=arr[i]
        minc+=1
print(maxc,minc)

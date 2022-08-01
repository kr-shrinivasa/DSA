n=int(input)
arr=list(map(int,input().split()))
arr.sort()
l,r=0,n-1
lv,rv=None,None
mii=float("inf")
while l<r:
    s=arr[l]+arr[r]
    if abs(s)<mii:
        mii=abs(s)
        lv=arr[l]
        rv=arr[r]
    if s==0:
        break
    if s<0:
        l+=1
    else:
        r-=1
print(lv,rv,mii)
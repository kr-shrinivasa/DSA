n,k=map(int,(input()).split())
arr=list(map(int,(input()).split()))
s=sum(arr)
z=0
for i in arr:
    if s-i==k:
        z=1
        break
print(z)



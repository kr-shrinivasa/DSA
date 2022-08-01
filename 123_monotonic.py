n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
c=1 
d=1 
for i in range(1,n):
    if arr[i]<=arr[i-1]:
        c+=1
    if arr[i]>=arr[i-1]:
        d+=1
# for i in range(1,n):
if c==n or d==n:
    print(True)
else:
    print(False)




arr=[]
n=int(input())
for i in range(n):
    arr.append(int(input()))
c=1
for i in range(1,n):
    if arr[i-1]<0 and arr[i]>0:
        c+=1
    if arr[i-1]>0 and arr[i]<0:

        c+=1
if c==n:
    print(True)
else:
    print(False)

    
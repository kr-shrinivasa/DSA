n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
f=-1
arr.sort()
for i in range(1,n):
    if arr[i]>arr[i-1]:
        c=n-i
        if c==arr[i-1]:
            f=1
            break
print(f)

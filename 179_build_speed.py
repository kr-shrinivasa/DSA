n=int(input())
arr=list(map(int,input().split()))
arr.sort()
s=0
for i in range(2*n):
    if i%2==0:
        s+=arr[i]
print(s)
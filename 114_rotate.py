arr=list(map(int,input().split()))
m=int(input())
n=len(arr)
f=[0]*n
for i in range(n):
    print((i-m)%n)
    f[(i-m)%n]=arr[i]
# i in f:
print(f)

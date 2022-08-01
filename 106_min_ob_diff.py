n=int(input())
arr=list(map(int,input().split()))
mi=10000
arr.sort()
for i in range(1,n):
    mi=min(mi,abs(abs(arr[i])-abs(arr[i-1])))
print(mi)  
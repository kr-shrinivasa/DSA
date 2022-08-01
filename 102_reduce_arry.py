def reduce(n,arr):
    if n==1:
        return arr[0]
    m=arr[0]+arr[1]
    for i in range(2,n):
        if i%2==0:
            m-=arr[i]
        else:
            m+=arr[i]
    return m


arr=[]
n=int(input())
for i in range(n):
    arr.append(int(input()))
print(reduce(n,arr))

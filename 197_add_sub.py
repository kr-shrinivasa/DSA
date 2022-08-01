def addi(arr,i,k):
    if (k==0 and i==len(arr)):
        return 1
    if i>=len(arr):
        return 0
    return (addi(arr,i+1,k)+addi(arr,i+1,k-arr[i])+addi(arr,i+1,k+arr[i]))
tar=int(input())
n=int(input())
arr=list(map(int,input().split()))
print(addi(arr,0,tar))

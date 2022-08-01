n=int(input())
arr=[0]
for i in range(n):
    arr.append(int(input()))
k=int(input())
i=k
s=0
while i<len(arr):
    s+=arr[i]
    i+=k
print(s)



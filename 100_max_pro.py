arr=[]
n=int(input())
for i in range(n):
    arr.append(int(input()))
arr.sort()
print(arr[-1]*arr[-2])

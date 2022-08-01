
n,k=map(int,input().split())
arr=[]
for i in range(n):
    s1=input()
    arr.append(s1)
b1=0
for i in range(k):
    for j in range(n-1):

        if arr[j][i]>arr[j+1][i]:
            b1+=1
            break
print(b1)
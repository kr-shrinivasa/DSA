n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
i=0
j=1
m=0
while i<n and j<n:
    
    if arr[j]-arr[i]>0:
        m=max(arr[j]-arr[i],m)
        print(m)
        
    else:
        i+=1
    j+=1
print(m)

    
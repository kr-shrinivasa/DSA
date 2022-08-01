n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
mn=int(input())
   
m=[]
for i in range(mn):
    m.append(int(input()))

c=0

if mn!=0:
    for i in range(n-mn+1):
        if arr[i:i+mn]==m:   
            c+=1
print(c)
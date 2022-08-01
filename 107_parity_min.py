arr=[]
n=int(input())
for i in range(n):
    arr.append(int(input()))
m=str(min(arr))

c=0
for i in m:
    c+=int(i)
if c%2==0:
    print(1)
else:
    print(0)

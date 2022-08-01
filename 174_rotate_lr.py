n,k=map(int,input().split())
arr=list(map(int,input().split()))
c=0
for i in range(k):
    a,b=input().split()
    if a=="L":
        c-=int(b)
    else:
        c+=int(b)
f=[0]*n
for i in range(n):
    f[(i+c)%n]=arr[i]
for i in f:
    print(i,end=" ")
        




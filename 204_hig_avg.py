def Where_to_place(l, x):
    s,e=0,len(l)-1
    while s<=e:
        mid=s+(e-s)//2
        if l[mid]<x:
            s=mid+1
        else:
            e=mid-1
    return s
   # Implement This
n=int(input())
l=list(map(int,input().split()))[:n]
sum=0
l.sort()
for i in range(n):
    sum+=l[i]
    avg=sum//(i+1)
    l[i]=avg   
t=int(input())    
for k in range(t):
    x=int(input())
    print(Where_to_place(l,x))
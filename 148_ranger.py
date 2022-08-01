for i in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))

    l=[1]
    r=[1]
    for i in range(1,len(arr)):
        l.append(l[-1]*arr[i-1])      
    for i in range(len(arr)-2,-1,-1):
        r.insert(0,r[0]*arr[i+1])
    for i in range(len(arr)):
        print(l[i]*r[i],end=" ")
for i in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    res=arr.sort()
    f=set()
    s=set()
    for i in range(0,n,2):
        f.add(arr[i])
        s.add(res[i])
    d=f-s
    print(len(s))
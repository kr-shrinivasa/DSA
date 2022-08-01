def xman(n,arr):
    s=sum(arr)/n
    c=0
    for i in arr:
        if i>s:
            c+=1
    return c


for i in range(int(input())):
    n=int(input())
    arr=list(map(int,(input()).split()))
    print(xman(n,arr))
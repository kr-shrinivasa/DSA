def xman(n,arr):
    c=arr[0]
    m=0
    for i in range(1,n):
        if arr[i]<0:
            m=max(m,c)
            c=0
        else:
            c+=arr[i]

    m=max(m,c)
    return masc



for i in range(int(input())):
    n=int(input())
    arr=list(map(int,(input()).split()))
    print(xman(n,arr))
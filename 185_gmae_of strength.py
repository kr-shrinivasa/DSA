def game(arr,n):
    arr.sort(reverse=True)
    s=n-1
    m=0
    for i in arr:
        m+=i*s
        s-=2
    res=m*max(arr)
    return res%1000000007



for i in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    print(game(arr,n))
for ne in range(int(input())):
    n=int(input())
    sa=0
    arr=[]
    for i in range(n):
        h,a=map(int,input().split())
        sa+=a
        arr.append(h+a)
    arr.sort(reverse=True)
    print(arr[0]+arr[1]-sa)
    
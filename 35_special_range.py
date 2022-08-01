def mn(m,n):
    if m<0:
        m=0
    if n<0:
        print(-1)
    else:
        for i in range(m,n+1):
            print(i)

m=int(input())
n=int(input())

mn(m,n)
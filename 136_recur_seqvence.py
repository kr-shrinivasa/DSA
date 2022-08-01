def recur(n):
    if n==1:
        return 1
    f=1
    s=((n-1)*(n)//2)+1
    e=s+n
    for i in range(s,e):
        f*=i
    return f+recur(n-1)



n=int(input())
print(recur(n))
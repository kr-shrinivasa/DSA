for i in range(int(input())):
    n=int(input())
    s=[]
    e=[]
    for i in range(n):
        a,b=map(int,input().split())
        s.append(a)
        e.append(b)
    s.sort()
    e.sort()
    i,j=0,0
    m=1
    while j<n:
        if e[j]>=s[i]:
            m=max(m.j-i)
            i+=1
        else:
            j+=1
    m=max(m,j-i)
    print(m)
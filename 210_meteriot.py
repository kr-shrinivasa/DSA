for _ in range(int(input())):
    n,m,q=map(int,input().split())
    x=set()
    y=set()
    for i in range(q):
        xx,yy=map(int,input().split())
        x.add(xx)
        y.add(yy)
    x.add(1)
    y.add(1)
    x.add(n)
    y.add(m)
    reg=(len(x)-1)*(len(y)-1)
    xma=0
    xmi=0
    yma=0
    ymi=0
    x=list(x)
    y=list(y)
    x.sort()
    y.sort()
    for x in range(len(x)-1):
        xma=max(xma,x[i+1]-x[i])
        xmi=min(xmi,x[i+1]-x[i])
    for x in range(len(y)-1):
        yma=max(yma,y[i+1]-y[i])
        ymi=min(ymi,y[i+1]-y[i])
    mina=xmi*ymi
    mana=xma*yma
    print(reg,mina,mana)


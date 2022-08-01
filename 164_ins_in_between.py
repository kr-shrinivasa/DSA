def inbetwwen(l,n,x):
    if x<=l[0]:
        return [x]+l
    elif x>=l[-1]:
        return l+[x]
    else:
        for i in range(1,n):
            if x<=l[i]:
                return l[:i]+[x]+l[i:]

n,x=map(int,input().split())
l=list(map(int,input().split()))
print(*inbetwwen(l,n,x))

n=int(input())
bt=[]
gt=[]
for i in range(n):
    g,k=map(int,input().split())
    if g==0:
        gt.append(k)
    else:
        bt.append(k)
gt.sort(reverse=True)
bt.sort(reverse=True)
print(*(gt+bt))



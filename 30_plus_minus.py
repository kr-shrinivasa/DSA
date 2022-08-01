n=int(input())
res=0
for i in range(n):
    if i%2==0:
        res+=int(input())
    else:
        res-=int(input())
print(res)
        
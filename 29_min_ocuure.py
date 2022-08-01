n=int(input())
p=int(input())
c=1
for i in range(n-1):
    r=int(input())
    if p==r:
        c+=1
print(c)
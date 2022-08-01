from collections import defaultdict
n=int(input())
order=[0]*n
for i in range(n):
    p,v=map(int,input().split())
    
    order[p]=v

ot=0
for i in range(1,n):
    vel=order[i]
    for j in range(i):
        if order[j]>vel:
            ot+=1
    
print(ot)




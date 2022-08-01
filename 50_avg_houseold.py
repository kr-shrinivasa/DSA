import math
income=[]
n=int(input())
for i in range(n):
    income.append(int(input()))
child=[]
for i in range(n):
    child.append(int(input()))
s=0
c=0
for i in range(n):
    if child[i]>2:
        s+=income[i]
        c+=1

if c==0:
    print(-1)
else:
    print(math.floor(s/c))




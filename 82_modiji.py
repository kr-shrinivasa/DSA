import math
n=int(input())
arr=list(map(int,input().split()))
s=0
for i in arr:
    s+=math.ceil(i*0.07)
print(s)

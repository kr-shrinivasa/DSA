v=int(input())

su=0
if v<0:
    n=v*-1
else:
    n=v
while n>0:
    t=n%10
    su=su*10+t
    n=n//10
if v>0:
    print(su)
else:
    print(-1*su)
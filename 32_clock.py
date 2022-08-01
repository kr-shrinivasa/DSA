a,b=map(int,input().split())
c=a+b

if sum%12==0:
    print(12)
else:
    print(sum%12)
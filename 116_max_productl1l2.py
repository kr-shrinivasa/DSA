m=int(input())
v=int(input())
lis1=list(map(int,input().split()))
lis2=list(map(int,input().split()))
m1=0
m2=0
for i in lis1:
    if abs(i)>m1:
        m1=abs(i)
for i in lis2:
    if abs(i)>m2:
        m2=abs(i)
print(m1*m2)

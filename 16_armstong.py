s=int(input())
n=s
e=0
while n>0:
    e+=(n%10)**3
    
    n=n//10
    
if e==s:
    print("Yes")
else:
    print("No")

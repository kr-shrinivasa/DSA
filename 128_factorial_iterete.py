n=int(input())
f="undefined"
if n==0 :
    f=1
elif n>1:
    f=1
    for i in range(1,n+1):
        f*=i
print(f)
n=int(input())
arr=list(map(int,input().split()))
arr.sort(reverse=True)
s1=0
s2=0
for i in range(n):
    if i%2==0:
        s1=s1*10+arr[i]
    else:
        s2=s2*10+arr[i]
print(s1+s2)
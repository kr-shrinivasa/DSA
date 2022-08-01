n=int(input())
arr=[]
for i in range(n):
    n,s,m=input().split()
    arr.append([n,int(s),int(m)])
arr.sort(key=lambda x:x[1])
arr.sort(key=lambda x:x[0])
arr.sort(key=lambda x:x[2],reverse=True)
[print(*i) for i in arr]
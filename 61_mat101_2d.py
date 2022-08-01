r,c=map(int,input().split())
#mat = [[int(input()) for x in range (c)] for y in range(r)]
c=0
for i in range(r):
        arr=list(map(int,input().split()))
        for i in arr:
            if i%2!=0:
                c+=i
print(c)
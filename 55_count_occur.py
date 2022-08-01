n=int(input())
c=0
l=[]
for i in range(n):
    l.append(int(input()))
q=int(input())
for i in l:
    if i==q:
        c+=1
print(c)
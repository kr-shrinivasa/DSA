n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
m=l[-1]
print(m)
for i in range(n-3,-1,-1):
    if l[i+1]>m:
        m=l[i+1]
        print(m)
  
    

    


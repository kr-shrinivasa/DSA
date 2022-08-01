n=int(input())
c=0
f=-1
for i in range(n):
    s=input()
    if s=="Toggle" and f==-1:
        f=1
        c+=1
        
    elif s=="Toggle" and f==1:
        f=-1
    elif s=="OFF" and f==1:
        f=-1
    elif s=="ON" and f==-1:
        c+=1
        f=1
        
print(c)
    

    
    
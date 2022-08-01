c=0
for i in range(int(input())):
    p=1
    s=0
    n=input()
    for i in n:
        p*=int(i)
        s+=int(i)
    if s>=p:
        c+=1
print(c)
    

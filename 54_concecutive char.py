s=input()
c=1
m=0
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        c+=1
    else:
        m=max(m,c)
        c=1
m=max(m,c)
print(m)

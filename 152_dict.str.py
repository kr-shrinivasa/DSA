

def long(s1,s2):
    m=0
    for i in s2:
        c=0
        for j in range(len(s1)):
            if i[c]==s1[j]:
                c+=1
        if c==len(i):
            
            m=max(m,len(i))
            break
    return m

s1=input()
s2=input().split()
print(long(s1,s2))


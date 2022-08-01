def half(s):
    h=len(s)//2
    lis=list(s[h:])
    for i in range(1,len(lis)):
        j=i
        while j>0 and lis[j]<lis[j-1]:
            lis[j],lis[j-1]=lis[j-1],lis[j]
            j-=1
    return s[:h]+"".join(lis)
print(half(input()))
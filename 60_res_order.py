torder=int(input())
tab=int(input())
num=[]
for i in range(torder):
    num.append(int(input()))

bill=[]
for i in range(torder):
    bill.append(int(input()))
val=[0]*(tab+1)
for i in range(torder):
    val[num[i]]+=bill[i]
ma=max(val)
for i in range(1,len(val)):
    if val[i]==ma:
        print(i)




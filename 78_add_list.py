# your code goes here
def addlist(arr1,arr2):
    res=[]
    c=0
    for i in range(len(arr1)):
        if i<len(arr2):
            t=arr1[i]+arr2[i]+c
        else:
            t=arr1[i]+c

        if t>=10:
            c=t//10
            t=t%10
        else:
        	c=0
        res.append(t)
    if c>0:
        res.append(c)
    for i in res:
        print(i,end="")
    print()
    
for i in range(int(input())):
    arr1=list(map(int,input().split()))
    arr2=list(map(int,input().split()))
    if len(arr2)>len(arr1):
        arr1,arr2=arr2,arr1

    addlist(arr1,arr2)


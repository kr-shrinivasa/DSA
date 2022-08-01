# your code goes here
from collections import defaultdict
def beauty(s):
    ca,cb,cc=0,0,0
    d=defaultdict(int)
    d[(0,0)]=1
    res=0
    for i in s:
        if i=="a":
            ca+=1
        elif i =="b":
            cb+=1
        elif i=="c":
            cc+=1
        z=(ca-cb,ca-cc)
        res+=d[z]

        d[z]+=1
    return res
    


for i in range(int(input())):
    s=input()
    print(beauty(s))
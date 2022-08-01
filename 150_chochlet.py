from collections import defaultdict
import math
from collections import Counter
def devisor(e):
    c=0
    
    for i in range(1,int(math.sqrt(e)+1)):
        if e%i==0:
            c+=1
            if e%i!=i:
                c+=1
    return c
        
def choch(n,arr):
    d=defaultdict(int)
    for i in arr:
        c=devisor(i)
        d[c]+=1
    r=0
    for i in d:
        r+=(d[i]*d[i]-1)//2
    return r
def negeted(num,arry):
    dict=Counter(arry)
    count=0
    for key in dict.keys():
        if key>0 and key*-1 in dict:
            
            count +=(dict[key] *dict[key]-1)//dict[(key*-1)]
        if key==0:
            count=(dict[key]*dict[(key*-1)])//2
    return count



n=int(input())
lst=list(map(int,input().split()))
print(choch(n,lst))
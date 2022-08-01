# your code goes here
from collections import defaultdict
def star(n):
    d=defaultdict(int)
    c=0

    for i in n:
        d[i]+=1
        if d[i]>=2:
            c+=d[i]-1
        
    return c




for i in range(int(input())):
	    
    s=int(input())
    n=input()
    print(star(n))
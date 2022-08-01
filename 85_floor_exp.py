
import math
def sumofproduct(n):
    s=0
    for i in range(1,n+1):
	    s+=(i*math.floor(n/i))
    return s
    
        


n = int(input())
print(sumofproduct(n))
#bells
import math
n = int(input())
array = [int(x) for x in input().split()]
ans = array[0]
if n==1:
	print(ans)
else:
    for i in range(n):
       gcd = math.gcd(ans,array[i])
       ans = ((ans*array[i])//gcd)
    print(ans)
# def sumofdivisors(n):
#     s=n
#     for i in range(1,int(n/2)+1):
#         if n%i==0:
#             s+=i
#     return s
#     # Code here
    

# n = int(input())
# print(sumofdivisors(n))
import math
def sumofdivisors(n):
    s=n
    for i in range(1,(n//2)+1):
        if n%i==0:
            s+=i
            
    return s
    # Code here
    

# n = int(input())
# print(sumofdivisors(n))

def devisor(e):
    c=0
    
    for i in range(1,int(math.sqrt(e)+1)):
        if e%i==0:
            c+=1
            if e%i!=i:
                c+=1
    return c
print(devisor(4))
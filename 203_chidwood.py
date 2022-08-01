# your code goes here
from collections import defaultdict
n = int(input())
A = [-1] * 256
d = defaultdict(int)
for i in range(n):
    a,b = input().lower().split()
    orda,ordb = ord(a),ord(b)
    A[ordb if d[ordb]==0 else d[ordb]] = orda
    A[orda if d[orda]==0 else d[orda]] = ordb
    d[ordb],d[orda] = orda if d[orda] == 0 else d[orda] , ordb if d[ordb]==0 else d[ordb]
com = list(input())
for i in range(len(com)):
    orrd = ord(com[i])
    if orrd>=65 and orrd<=90:
        if A[ord(com[i].lower())] != -1:
            com[i] = chr(A[ord(com[i].lower())])
        com[i] = com[i].upper()
    else:
        if A[ord(com[i].lower())] != -1:
            com[i] = chr(A[ord(com[i].lower())])
print("".join(com))
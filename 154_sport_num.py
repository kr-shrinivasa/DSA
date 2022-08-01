# your code goes here
from collections import Counter
n=int(input())
dict={}
for i in range(n):
    v=list(input().split(" "))
    dict[v[0]]=v[1]


dict1=Counter(dict.values())


c=0
g=""
for i in dict1:
    if dict1[i]>c:
        c=dict1[i]
        g=i
    elif dict1[i]==c:
        if ord(i[0])<ord(g[0]): #or if i<g:
            g=i
            
print(g)
print(dict1["football"])




from collections import Counter

d=[]
for i in range(int(input())):
    d.append(int(input()))
di=Counter(d)

for i in (di):
    if di[i]==1:
        print(i)
        break

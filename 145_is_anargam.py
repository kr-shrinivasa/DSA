from collections import Counter
def st(s1,s2):

    d1=Counter(s1)
    d2=Counter(s2)
    if len(s1)!=len(s2):
        return 0
    for i in s2:
        if i not in d1:
            return 0
        if d2[i]!=d1[i]:
            return 0
    return 1


s1=input()
s2=input()
print(st(s1,s2))
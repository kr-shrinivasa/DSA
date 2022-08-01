#groups of anagram.
from collections import Counter
def groupAnagrams(arr):
    d={}
    arr.sort()
    for x in arr:
        a = "".join(sorted(x))
        if a not in d:
           d[a]=[x]
        else:
           d[a].append(x)
    res=[]
    for x in d:
        res.append(sorted(d[x]))
    if len(d)==0:
        return [[""]]
    return res
if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        arr = input().split()
        print(groupAnagrams(arr))
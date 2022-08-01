from collections import Counter
def bothCountX(string1, string2, x):
    
    d1=Counter(string1)
    d2=Counter(string2)
    arr=[]
    for i in d1:
        if d1[i]==x and d2[i]==x:
            if 97<=ord(i)<=122:
                arr.append(i)
    arr.sort()
    return arr


    # Complete this function, and return the list of resultant characters in sorted order

for _ in range(int(input())):
    string1, string2, x = input().split()
    x = int(x)
    string1=string1.lower()
    string2=string2.lower()
    print(*bothCountX(string1, string2, x))
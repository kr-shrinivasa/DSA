def rever(s):
    if len(s)==1:
        return s
    r=s[-1]
    r+=rever(s[:-1])
    return r

for i in range(int(input())):
    s=input()
    print(rever(s))
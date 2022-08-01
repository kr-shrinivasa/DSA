def rever(s):
    if len(s)==1:
        return int(s)
    return int(s[-1])*rever(s[:-1])


for i in range(int(input())):
    s=input()
    print(rever(s))
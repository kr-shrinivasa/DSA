def rever(s):
    if s<=9:
        return s
    if s%2==0:
        return rever(s-10)
    return rever(s-9)


for i in range(int(input())):
    s=int(input())
    print(rever(s))
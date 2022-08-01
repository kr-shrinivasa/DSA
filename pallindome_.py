for i in range(int(input())):
    s=input()
    s=s.lower()

    r=""
    for i in range(len(s)):
        if s[i]>="a" and s[i]<="z":
            r+=s[i]
    if r==r[::-1]:
        print(True)
    else:
        print(False)



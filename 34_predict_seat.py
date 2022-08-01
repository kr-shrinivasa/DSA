n=int(input())
for i in range(n):
    c,b=map(int,input().split())
    if b>c:
        print("Invalid")
    elif b%8==0:
        print("SU")
    elif b%8==1 or b%8==4:
        print("L")
    elif b%8==2 or b%8==5:
        print("M")
    elif b%8==3 or b%8==6:
        print("U")
    else:
        print("SL")
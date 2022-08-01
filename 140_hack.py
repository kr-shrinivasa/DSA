def hack(n):
    if n==0:
        return False
    if n==1:
        return True
    if n%10==0 and n%20==0:
        return hack(n//10) or hack(n//20)
    elif n%10==0:
        return hack(n//10)
    elif n%20==0:
        return hack(n//20)
    else:
        return False
for i in range(int(input())):
    n=int(input())       
    print("Yes" if hack(n) else "No")

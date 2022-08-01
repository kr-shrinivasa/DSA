import math
for i in range(int(input())):

    n=int(input())
    if n==0 or n==1:
        print("No")
        
    elif n==2 and n==3:
        print("Yes")

    else:
        for i in range(2,int(math.sqrt(n))+1):
            if n%i==0:
                print("No")
                break
        else:
            print("Yes") 
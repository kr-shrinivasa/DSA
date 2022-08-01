for i in range(int(input())):

    a,b=map(int,input().split())
   

    gcd=0
    while True:
        if b==0:
            gcd=0
            break
        c=a%b
        if c==0:
            gcd=b
            break
        else:
            a=b
            b=c
    print(gcd)
         
        

         


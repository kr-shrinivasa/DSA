n=int(input())
tribo=[0,0,1]
if n<=3:
    print(tribo[n-1])
else:
    for i in range(n-3):
        tribo[(i%3)]=tribo[-1]+tribo[-2]+tribo[-3]
        
    print(tribo[(n%3)-1])
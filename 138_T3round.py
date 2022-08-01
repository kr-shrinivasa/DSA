def roundy(n,arr):
    ar=[]
    if n==1:
        ar=[-1]
        
    for i in range(n-1):
        if arr[i]==0:
            ar=[-1]
            
        else:
            ar.append(round(arr[i+1]/arr[i]))
    print(*ar)




for i in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    roundy(n,arr)
    
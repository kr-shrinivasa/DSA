n=int(input())
arr=list(map(int,input().split()))
mini=[]
maxi=[]
c=0
for i in range(n):
    mini.append(min(i+1,arr[i]))
    maxi.append(max(i+1,arr[i]))
    c+=abs(i+1-arr[i])
c+=2*(max(mini)-min(maxi))
print(c)

    

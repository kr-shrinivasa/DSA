n=int(input())
arr=list(map(int,input().split()))

end=0
ma=0
leth=1

for i in range(1,n):
    if arr[i]>arr[i-1]:
        leth+=1
    else:
        if leth>ma:
            ma=leth
            end=i
        leth=1
if leth>ma:
    ma=leth
    end=n
print(ma,end-ma+1,end)
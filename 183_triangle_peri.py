
def tru(arr):
    arr.sort(reverse=True)
    f=0
    i,j,k=0,1,2
    while i<len(arr) and j<len(arr)and k<len(arr):
        if arr[j]+arr[k]>arr[i]:
            f= arr[j]+arr[k]+arr[i]
            break

        i+=1
        j+=1
        k+=1
    return f
            
noftestcases = int(input())
for i in range(noftestcases):
    arr = list(map(int, input().split()))
    print(tru(arr))
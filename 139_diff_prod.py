def minDiff(arr, arr_size):
    arr.sort()
    mini=10000
    for i in range(1,arr_size):
        mini=min(mini,arr[i]-arr[i-1])

    return mini
    


def maxDiff(arr, arr_size):
    return max(arr)-min(arr)
	

def prodDiff(arr, arr_size):
    if arr_size<=1:
        return "NA"
    return maxDiff(arr,arr_size)*maxDiff(arr,arr_size)
	### Complete this anarrd the above functions!

for _ in range(int(input())):
    length = int(input())
    arr = [int(x) for x in input().split()]
    print(prodDiff(arr, length))
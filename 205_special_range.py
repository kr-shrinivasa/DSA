def first(array,n,left):
    l = 0
    r = n - 1
    res = -1
    while l<=r:
        mid = (l+r) // 2
        if array[mid] >= left:
            res = mid
            r = mid - 1
        else:
            l = mid + 1
    return res
def last(array,n,right):
    l = 0
    r = n - 1
    res = -1
    while l<=r:
        mid = (l+r) // 2
        if array[mid] <= right:
            res = mid
            l = mid + 1
        else:
            r = mid - 1
    return res
n = int(input())
array = [int(x) for x in input().split()]
left,right = map(int, input().split())
a,b = first(array,n,left) , last(array,n,right)
if a<=b:
    print(a,b)
else:
    print(-1,-1)
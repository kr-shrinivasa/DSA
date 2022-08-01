def indexnsertindexonSort(arr, n):
    for j  in range(1,n):
        j=index
        while index>0 and arr[index]<arr[index-1]:
            arr[index-1],arr[index]=arr[index],arr[index-1]
            index-=1
    return arr




if __name__ == '__maindexn__':
    
    n = int(input())
    arr = [int(x) for x in input().split()]
    print(*indexnsertindexonSort(arr, n))
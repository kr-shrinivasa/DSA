for i in range(int(input())):

    arr=list(map(int,input().split()))
    even=[]
    odd=[]
    for i in range(len(arr)):
        if i%2==0:
            even.append(arr[i])
        else:
            odd.append(arr[i])
    even.sort(reverse=True)
    odd.sort()
    for i in range(len(even)):
        arr[i*2]=even[i]
    for i in range(len(odd)):
        arr[i*2+1]=odd[i]
    print(*arr)

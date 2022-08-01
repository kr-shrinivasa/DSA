n1 = int(input())
arr1 = []
for i in range(n1):
    arr1.append(int(input()))
n2 = int(input())
arr2 = []
for i in range(n2):
    arr2.append(int(input()))
arr3 = []
n3 = int(input())
for i in range(n3):
    arr3.append(int(input()))

if len(arr1)>=1 and len(arr2)>=1 and len(arr3)>=1:
    res = []
    for i in arr2:
        if i in arr3 and i in arr1:
            res.append(i)
    if res == []:
        print(-1)
    else:
        for ele in res:
            print(ele)
else:
    print(-1)
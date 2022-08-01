def zeroSum(matrix, rows, cols):
    c=0
    for i in range(rows):
        s=0
        for j in range(cols):
            s+=matrix[i][j]
        if s==0:
            c+=1
    for i in range(cols):
        s=0

        for j in range(rows):
            s+=matrix[j][i]
        if s==0:
            c+=1 
    return c  



for _ in range(int(input())):
    n,m = map(int, input().split())
    arr = [[int(x) for x in input().split()] for i in range(n)]
    print(zeroSum(arr, n, m))
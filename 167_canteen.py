n,k=map(int,input().split())
arr=list(map(int,input().split()))
charge=int(input())
act=(sum(arr)-arr[k])/2
if charge==int(act):
    print("It is Correct!")
else:
    print(charge-int(act))


n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
m=int(input())

for f in range(m):
    fold=[]
    for i in range(len(arr)//2):
        a=arr[i]+arr[len(arr)-i-1]

        fold.append(a)
    if len(arr)%2!=0:
        fold.append(arr[(len(arr)//2)])
    arr=fold
print(len(arr))
for i in arr:
    print(i)


# # your code goes here
# n=int(input())
# aee=[]
# for i in range(n):
#     aee.append(int(input()))
# m=int(input())
# for i in range(m):
#     if len(aee)%2!=0:
#         r= len(aee)//2+1
#     else:
#         r=len(aee)//2
    	
#     abb=[]
    
#     for j in range(r):
#         if j!=(len(aee)-1-j):
#             c=aee[j]+aee[len(aee)-1-j]
#             abb.append(c)
#         else:
#             abb.append(aee[j])
    
#     aee=abb

# print(len(aee))
# for i in aee:
#     print(i)

    

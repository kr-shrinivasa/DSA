# n,k=map(int,input().split())
# mat=[]
# for i in range(n):
#     mat.append(i)
#     arr=list(map(int,input().split()))
#     mat[i]=arr
# ar=list(map(int,input().split()))
# # final=[]
# for i in range(ar[2]-1,ar[3]):
#     # final.append(i)
#     # s=[]
#     for j in range(ar[0]-1,ar[1]):
        
#         s.append(mat[i][j])
#     final[i]=s

# for i in range(len(final)):
#     print(*final[i])
#write your code here
n,k=map(int,input().split())
mat=[]
for i in range(n):
    arr=list(map(int,input().split()))
    mat.append(arr)
    
ar=list(map(int,input().split()))

for i in range(ar[2]-1,ar[3]):

    for j in range(ar[0]-1,ar[1]):
        print(mat[i][j],end=" ")
    print()
       
    









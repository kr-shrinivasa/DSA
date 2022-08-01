# n=int(input())
# arr=list(map(int,input().split()))
# s=0
# for i in range(n-1):
#     for j in range(i+1,n):
#         s=s+abs(arr[i]*arr[j])
# # print(s)
n = int(input())
arr = list(map(int, input().split()))
su = 0

for i in arr:
    su = su + abs(i)

sq = 0
for i in arr:
    sq = sq + (i*i)

res = ((su**2) - sq) // 2
print(res)

n, q = map(int, input().split())
a = input()
b = input()
queries = []
for i in range(q):
    queries.append(int(input()))
def check(mid):
    s = list(b)
    for i in range(mid+1):
        s[queries[i]-1] = "1"
    s = "".join(s)
    return s>=a
l = 0
r = n -1
res = -1
while l <= r:
    mid = l + (r-l)//2
    if check(mid):
        res = mid
        r = mid - 1
    else:
        l = mid + 1
ans = ["NO"] * q
if res != -1:
    for i in range(res,q):
        ans[i] = "YES"
for ele in ans:
    print(ele)
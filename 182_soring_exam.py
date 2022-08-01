n,k=map(int,input().split())
time=list(map(int,input().split()))
score=list(map(int,input().split()))
time.sort(reverse=True)
cs=[time[0]]

for i in range(1,n):
    cs.append(cs[-1]+time[i])
for i in range(k):
    v=int(input())
    print(cs[v-1])


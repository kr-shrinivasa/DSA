n=int(input())
mini=float("inf")
maxi=0
for i in range(n):
    p=int(input())
    mini=min(mini,p)
    maxi=max(maxi,p)
print(mini*maxi)

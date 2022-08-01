def make(s,n):
    if len(s)<=1:
        return s
    if n==0:
        return s+s[::-1]
    if n==1:
        return s+s[-2::-1]
   
s=input()
n=int(input())
print(make(s,n))

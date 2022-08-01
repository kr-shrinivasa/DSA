n=int(input())
l=[]
for i in range(n):
    l.append(int(input())**2)
l.sort()
for i in l:
    print(i)
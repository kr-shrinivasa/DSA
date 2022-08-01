# from collections import Counter
# n=int(input())
# s=input().split()
# d=Counter(s)
# f=0
# for i in d:
#     if d[i]>n:
#         f=1
#         print(i)
# if not f:
#     print("no such names in this town!!!")


from collections import Counter

n=int(input())
x=int(input())

arr=list(map(int,input().split()))
d=Counter(arr)

remain=[]
state =[]
centarl =[]
for i in range(n):
    if i not in d:
        remain.append(i)
for i in range(len(remain)):
    if i%2==0:
        centarl.append(remain[i])
    else:
        state.append[remain[i]]
        
print("c:",*centarl,"s:",*state)

# print(f"c:{*} and I'm {age} years old.")
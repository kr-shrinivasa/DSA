# from collections import Counter
# n=int(input())

# arr=[]
# for i in range(n):
#     arr.append(int(input()))
# d=Counter(arr)
# p=-1
# for i in d:
#     if d[i]==4:
#         p=i
#         break
# print(p)
n=int(input())

arr=[]
for i in range(n):
    arr.append(int(input()))
c=1
p=-1
for i in range(1,n):
    if arr[i]==arr[i-1]:
        c+=1
        print(c)
    elif c==4:
        p=arr[i-1]
        break
    else:
        c=1
print(i)
if c==4 and i==n-1:
    p=arr[-1]
print(p)


   
    
    


    
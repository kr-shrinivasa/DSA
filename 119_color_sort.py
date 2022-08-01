# arr=[]
# n=int(input())
# for i in range(n):
#     arr.append(int(input()))
# f=[0,0,0]
# for i in arr:
#     f[i]+=1
# for i in range(f[0]):
#     print(0)
# for i in range(f[1]):
#     print(1)
# for i in range(f[2]):
#     print(2)

# your code goes here
# def colorsort():
#     count =[0,0,0]


# n=int(input())
# arr=[]
# for _ in range(n):
#     arr.append(int(input()))
# colorsort()

# your code goes here
def colorsort():
	count =[0,0,0]
	for num in arr:
		if num==0:
			count[num]+=1
		elif num==1:
			count[num]+=1
		else:
			count[num]+=1
	for i in range(count[0]):
		print(0)
	for i in range(count[1]):
		print(1)
	for i in range(count[2]):
		print(2)

n=int(input())
arr=[]
for _ in range(n):
	arr.append(int(input()))
colorsort()
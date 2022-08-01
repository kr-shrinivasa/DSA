n=int(input())
ma=0
for i in range(n):
    ma+=int(input())
if ma/n>100:
    print("Excellent!")
else:
    print("Not Excelent!")

def dis(num):
    if num<=2:
        return num
    return dis(num-1)+dis(num-2)
for i in range(int(input())):
    print(dis(int(input())))
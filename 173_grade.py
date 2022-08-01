def grade(num):
    if num<38:
        return num
    if (num+1)%5==0:
        return num+1
    if (num+2)%5==0:
        return num+2
    return num
for i in range(int(input())):
    print(grade(int(input())))
    
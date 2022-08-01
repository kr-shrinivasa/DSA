# name your function as change_diagonal and it should take list as input
def change_diagonal(lst):
    for i in range(len(lst)):
        d=lst[i][i]
        
        if d<0:
            lst[i][i]=0
        elif d>=0:
            lst[i][i]=1
    return lst
        
            
        
        
    




# Do not change anything below this line.
if __name__ == "__main__":
    val = int(input())
    lst = []
    for index in range(0, val):
        lst.append([int(i) for i in input().split(' ')])
    out = change_diagonal(lst)
    for lst1 in out:
        # print(" ".join(str(i) for i in lst1))
        print(*lst1)

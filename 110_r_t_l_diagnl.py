# name your function as right_to_left_diagonal
def right_to_left_diagonal(lst):
    s=0
    for i in range(len(lst)):
        s+=lst[i][(len(lst)-1-i)]
        s+=lst[i][i]
    


# Do not change anything below this line
if __name__ == "__main__":
    m = int(input())
    lst = []    
    for val in range(0, m):
        lst.append([int(i) for i in input().split(' ')])
    out = right_to_left_diagonal(lst)
    [print(val) for val in out]
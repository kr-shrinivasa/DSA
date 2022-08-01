# name you function as transpose_matrix and takes a list
# you should return a list of lists
def transpose_matrix(mat):
    t=[]
    for i in range(len(mat[0])):
        t.append(i)
        a=[]
        for j in range(len(mat)):
            
            a.append(mat[j][i])
        t[i]=a
        
    return t



# do not change anything below this line
if __name__ == "__main__":
    h = int(input())
    lst = []
    for val in range(0, h):
        lst.append([int(i) for i in input().split(' ')])
    out = transpose_matrix(lst)
    for val in out:
        print(" ".join(str(i) for i in val))
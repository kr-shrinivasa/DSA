# your code goes here
def intToArr(N):
    arr=[]
    for i in str(N):
        if int(i)!=3:

            arr.append(int(i))
    return arr
    
    #complete this function

def remove_3(arr):
    
    
    return arr
    #complete this function

def arrToInt(arr):
    s=0
    for i in arr:
        s=s*10+i
    return s
        
        

        


    #complete this function

#DO NOT change anything below this line

N=int(input())
arrNum=intToArr(N)
arrNumWithout3=remove_3(arrNum)

print(arrToInt(arrNumWithout3))
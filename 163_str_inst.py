def stringInsertionSort(str):
    arr=[]
    for i in str:
        arr.append(i)
    # Your code goes here
    for j in range(1,len(arr)):
        i=j
        while i>0 and ord(arr[i])< ord(arr[i-1]):
            arr[i-1],arr[i]=arr[i],arr[i-1]
            i-=1
    s1=""
    for i in arr:
        s1+=i
    return s1


### DO NOT CHANGE ANYTHING BELOW THIS LINE

if __name__=='__main__':
    input_string = input()
    print(stringInsertionSort(input_string))

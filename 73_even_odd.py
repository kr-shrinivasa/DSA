# Write a function with name even_odd_separator, you should exactly the same name
# This even_odd_separator functions should take a list of integers and return a list
# you can start from here	
def even_odd_separator(numbers):
    i,j=0,len(numbers)-1
    while i<j:
        if numbers[i]%2==0 and numbers[j]%2!=0:
            numbers[i],numbers[j]=numbers[j],numbers[i]
            i+=1
            j-=1
        elif numbers[i]%2==0 and numbers[j]%2==0:
            j-=1
        elif numbers[i]%2!=0 and numbers[j]%2==0:
            j-=1
            i+=1
        elif numbers[i]%2!=0 and numbers[j]%2!=0:
            i+=1                     

    return numbers


### Do not change anything below this line
if __name__ == "__main__":
    numbers = [int(i) for i in input().split(' ')]
    separated = even_odd_separator(numbers)
    for num in separated:
    	print(num)
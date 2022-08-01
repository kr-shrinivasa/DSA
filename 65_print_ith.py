#You have writer a function with function name as printer which takes a list.
# you can use print_with_index to print
# You can start from below
def printer(arr):
    for i in range(len(arr)):
        print_with_index(i,arr[i])



# Do not change anything below this line
def print_with_index(index, current_string):
    print(index, current_string)

if __name__ == "__main__":
    count = int(input())
    input_list = [input() for i in range(count)]
    printer(input_list)
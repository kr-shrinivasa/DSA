# Fill in the following function.
# Please do not change the function name.
def signum(number):
    if number<0:
        return -1
    if number>0:
        return 1
    if number==0:
        return 0
    # you can start from here.



### Please do not edit the code below this line.

if __name__ == "__main__":
    test_input = float(input())
    print(signum(test_input))
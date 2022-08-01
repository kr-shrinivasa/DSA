def shuffle(arr):
    ele=[]
    n=len(arr)//2

    for i in range(n):
        ele.append(arr[i])
        ele.append(arr[n+i])
    return ele

    # Implement this function

# Do not edit anything below
if __name__ == "__main__":
    n = int(input())
    nums = []
    for index in range(2 * n):
        nums.append(int(input()))
    for elem in shuffle(nums):
        print(elem)
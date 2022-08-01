


def findLuckyNumber(nums):
    c=1
    
    if len(nums)==1 and nums[0]==1:
        return nums[0]
    for i in range(len(nums)-1):
        if nums[i]!=nums[i+1]:
            if c==nums[i]:
                return nums[i]
            c=1
        else:
            c+=1
    if c>1 and c==nums[-1]:
        return nums[-1]
    return -1
          # implement this function

# DO NOT change anything below this line
if __name__ == "__main__":
    num_elems = int(input())
    input_arr = []
    for index in range(num_elems):
        input_arr.append(int(input()))
    
    print(findLuckyNumber(input_arr))
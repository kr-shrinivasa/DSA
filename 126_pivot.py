


# lsum=[0]
# for i in range(n-1):
#     lsum.append(lsum[-1]+nums[i])
# print(lsum)
# rsum=[0]
# for i in range(n-1,0,-1):
#     rsum.append(rsum[-1]+nums[i])
# print(rsum)


# for i in range(n):
#     if lsum[i]==rsum[n-1-i]:
#             p=i
#             break
# print(p)

        

def pivotIndex(arr):
    # Implement this function   
    cu=[arr[0]]
    p=-1
    for i in range(1,len(arr)):
        cu.append(cu[-1]+arr[i])

    if len(arr)==1:
        p=0
        return p


    for i in range(len(arr)):
        if i==0:
            if cu[-1]-cu[i]==0:
                p=i
                return p
        elif i==len(arr)-1:
            if cu[i-1]==0:
                p=i
                return p

        else:
            if cu[i-1]==cu[-1]-cu[i]:
                p=i
                return p
    if p==-1:
        return p        




# Do not edit anything below
if __name__ == "__main__":
    num_elems = int(input())
    nums = []
    for i in range(num_elems):
        nums.append(int(input()))

    print(pivotIndex(nums))
def pivotIndex(arr):
    # Implement this function
    p=-1
    lsum=[0]
    n=len(arr)
    for i in range(n-1):
        lsum.append(lsum[-1]+arr[i])

    rsum=[0]
    for i in range(n-1,0,-1):
        rsum.append(rsum[-1]+arr[i])

    for i in range(n):
        if lsum[i]==rsum[n-1-i]:
                p=i
                break
    return p
# Do not edit anything below
if __name__ == "__main__":
    num_elems = int(input())
    nums = []
    for i in range(num_elems):
        nums.append(int(input()))
        
    print(pivotIndex(nums))
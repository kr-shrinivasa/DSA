from collections import Counter
def intersect(nums1, nums2):
    # implement this function
    d=Counter(nums1)

    t=Counter(nums2)
    for i in d:
        if t[i]==0:
            d[i]=-1
        else:
            d[i]=min(d[i],t[i])
    res=[]
    for k,v in sorted(d.items()):
        if v!=-1:
            res.append(k)
            res=res[-1]*v
    if res==[]:
        res.append(-1)
    return res

# DO NOT change anything below this line
if __name__ == "__main__":
    num1_len = int(input())
    nums1 = []
    for index in range(num1_len):
        nums1.append(int(input()))
    num2_len = int(input())
    nums2 = []
    for index in range(num2_len):
        nums2.append(int(input()))
    for element in intersect(nums1, nums2):
        print(element)
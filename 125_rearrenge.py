# your code goes here
n=int(input())
nums=[]
ind=[]
for i in range(n):
    nums.append(int(input()))
for i in range(n):
    ind.append(int(input()))
tar=[]
for i in range(n):
    if ind[i]>=len(tar):
    	tar.append(nums[i])
    else:
        tar.insert(ind[i],nums[i])    
        
    # else:
    #     tar.append(nums[i])
    #     for j in range(len(tar)-2,ind[i]-1,-1):
    #     	tar[j+1]=tar[j]
    #     tar[ind[i]]=nums[i]
        

        
for i in tar:
    print(i)
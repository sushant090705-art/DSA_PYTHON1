nums=[5,6,7,5,4,3,2,4,4,5,6]
n=len(nums)
temp=nums[n-1]
for i in range(n-2,-1,-1):
    nums[i+1]=nums[i]
nums[0]=temp  
print(nums)  
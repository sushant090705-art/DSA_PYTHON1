nums=[4,6,4,2,7,2,9,4]
largest=nums[0]
n=len(nums)
for i in range (0,n):
    largest=max(largest,nums[i])
print(largest)
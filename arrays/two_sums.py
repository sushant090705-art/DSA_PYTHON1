#bruteforce solution
nums=[2,7,1,8]
target=9
class Solution(object):
    def twoSums(self,nums,target):
        n=len(nums)
        for i in range(0,n-1):
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    return [i,j]
obj = Solution()
print(obj.twoSums(nums,target))          
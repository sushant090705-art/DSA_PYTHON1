# nums=[1,2,3,4,5,6,7]
# class Solution(object):
#     def rotate(self, nums, k):
#         n=len(nums)
#         rotation=k%n
#         for _ in range (0,rotation):
#             e=nums.pop()
#             nums.insert(0,e)
# obj=Solution()
# obj.rotate(nums,3)
# print(nums)

#optimal
class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n

        nums.reverse()

        nums[:k] = reversed(nums[:k])

        nums[k:] = reversed(nums[k:])
# nums=[1,1,3,3,4,5,6,7,7,8,9]
# n=len(nums)
# dict={}
# for i in range (0,n):
#     dict[nums[i]]=0
# j=0
# for k in dict:
#     nums[j]=k
#     j+=1
# print(j) 

#another solution
# class Solution(object):
#     def removeDuplicates(self, nums):
#         if len(nums) == 0:
#             return 0

#         j = 0

#         for i in range(1, len(nums)):
#             if nums[i] != nums[j]:
#                 j += 1
#                 nums[j] = nums[i]

#         return j + 1 

# #brute force
# nums=[1,-2,-2,-4,2,7]
# pos=[1,2,7]
# neg=[-2,-2,-4]
# n=len(nums)
# for i in range(0,len(pos)):
#     nums[2*i]=pos[i]
#     nums[(2*i)+1]=neg[i]
# print(nums)    


#optimal
nums=[1,2,-4,-5,5,-6]
n=len(nums)
result=[0]*n
posindex=0
negindex=1
for i in range(0,n):
    if nums[i]>=0:
        result[posindex]=nums[i]
        posindex+=2
    else:
        result[negindex]=nums[i]
        negindex+=2
print(result)        

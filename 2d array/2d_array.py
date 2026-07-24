# # nums=[[1,2,3],[4,3,1],[9,7,6]]
# # n=len(nums)
# # rows=len(nums)
# # cols=len(nums[0])
# # for i in range(0,rows):
# #     for j in range(0,cols):
# #         print(nums[i][j],end=" ")
# #     print()    


# #upper triangle
# # nums=[[1,2,3],[4,3,1],[9,7,6]]

# # rows=len(nums)
# # cols=len(nums[0])
# # for i in range(0,rows):
# #     for j in range(0,cols):
# #         if j>=i:
# #          print(nums[i][j],end=" ")
# #         else:
# #            print("*",end=" ")
# #     print()       
     

# #lower triangle
# # nums=[[1,2,3],[4,3,1],[9,7,6]]

# # rows=len(nums)
# # cols=len(nums[0])
# # for i in range(0,rows):
# #     for j in range(0,cols):
# #         if j<=i:
# #          print(nums[i][j],end=" ")
# #         else:
# #            print("*",end=" ")
# #     print()   


# #print diagonal
# nums=[[1,2,3],[4,3,1],[9,7,6]]

# rows=len(nums)
# cols=len(nums[0])
# for i in range(0,rows):
#     for j in range(0,cols):
#         if j==i:
#          print(nums[i][j],end=" ")
#         else:
#            print("*",end=" ")
#     print()   

nums=[[1,2,3],[4,3,1],[9,7,6]]

rows=len(nums)
cols=len(nums[0])
for i in range(0,rows):
    for j in range(0,cols):
        if  j<=i  and j>=i:
         print(nums[i][j],end=" ")
        else:
           print("*",end=" ")
    print()   
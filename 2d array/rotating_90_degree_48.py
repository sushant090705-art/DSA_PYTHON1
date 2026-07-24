class Solution(object):
    def rotate(self, matrix):
        n=len(matrix)
        result=[[0 for _ in range(n)]for _ in range(n)]
        for i in range(0,n):
            for j in range(0,n):
              result[j][(n-1)-i]=matrix[i][j]
        return result    
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

obj = Solution()
ans = obj.rotate(matrix)

print("Original Matrix:")
for row in matrix:
    print(row)

print("\nRotated Matrix:")
for row in ans:
    print(row)
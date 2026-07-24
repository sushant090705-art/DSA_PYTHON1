class Solution:
    def markInfinity(self, matrix, row, col):
        r = len(matrix)
        c = len(matrix[0])

        # Mark the column
        for i in range(r):
            if matrix[i][col] != 0:
                matrix[i][col] = float("inf")

        # Mark the row
        for j in range(c):
            if matrix[row][j] != 0:
                matrix[row][j] = float("inf")

    def setZeroes(self, matrix):
        r = len(matrix)
        c = len(matrix[0])

        # Mark cells as infinity
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    self.markInfinity(matrix, i, j)

        # Convert infinity to zero
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == float("inf"):
                    matrix[i][j] = 0


# Driver Code
matrix = [
    [1, 1, 1], [1, 0, 1],[1, 1, 1]
]

print("Original Matrix:")
for row in matrix:
    print(row)

obj = Solution()
obj.setZeroes(matrix)

print("\nOutput Matrix:")
for row in matrix:
    print(row)
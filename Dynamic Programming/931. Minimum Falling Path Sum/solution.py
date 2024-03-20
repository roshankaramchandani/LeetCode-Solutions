class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        if n==1:
            return matrix[0][0]
        for i in range(n-2, -1, -1):
            for j in range(n-1,-1,-1):
                if 0<j<n-1:
                    matrix[i][j] += min(matrix[i+1][j], matrix[i+1][j-1], matrix[i+1][j+1])
                elif j==0:
                    matrix[i][j] += min(matrix[i+1][j], matrix[i+1][j+1])
                else:
                    matrix[i][j] += min(matrix[i+1][j], matrix[i+1][j-1])
        return min(matrix[0])
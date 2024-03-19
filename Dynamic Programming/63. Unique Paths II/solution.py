class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        memo = {}
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        def solve(i,j):

            if (i,j) in memo:
                return memo[(i,j)]
            if i==m-1 and j==n-1:
                if obstacleGrid[i][j] == 1:
                    return 0
                return 1
            
            if i==m or j==n or obstacleGrid[i][j] == 1:
                memo[(i,j)] = 0
                return 0
            
            memo[(i,j)] = solve(i+1,j) + solve(i,j+1)
            return memo[(i,j)]
        
        return solve(0,0)


                

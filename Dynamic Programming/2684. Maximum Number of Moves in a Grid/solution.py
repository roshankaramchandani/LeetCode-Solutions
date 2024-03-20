class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        dp = [[0]*col for _ in range(row)]
        directions = [[0,1],[1,1],[-1,1]]

        for j in range(col-2,-1,-1):
            for i in range(row-1,-1,-1):
                for dx,dy in directions:
                    newI = i+dx
                    newJ = j+dy
                    if 0<=newI<row and grid[newI][newJ]>grid[i][j]:
                        dp[i][j] = max(dp[i][j],1+dp[newI][newJ])

        ans = 0
        for i in range(row):
            ans = max(ans,dp[i][0])
        return ans
                        
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        ans = 1
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[-1]*cols for _ in range(rows)]

        def dfs(i,j):
            nonlocal dp
            directions = [[0,1],[0,-1],[1,0],[-1,0]]
            curr = 1
            for dx,dy in directions:
                newI = i+dx
                newJ = j+dy

                if 0<=newI<rows and 0<=newJ<cols and matrix[newI][newJ]>matrix[i][j]:
                    if dp[newI][newJ]==-1:
                        tempAns = dfs(newI,newJ)
                        dp[newI][newJ] = tempAns
                        curr = max(curr,1+tempAns)
                    else:
                        curr = max(curr,1+dp[newI][newJ])
            return curr




        for i in range(rows):
            for j in range(cols):
                if dp[i][j] == -1:
                    dp[i][j] = dfs(i,j)
                
                ans = max(ans,dp[i][j])
        print(dp)
        return ans
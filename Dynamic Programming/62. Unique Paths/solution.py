class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def solve(i, j, m, n):
            if (i,j) in memo:
                return memo[(i,j)]
            if i==m and j==n:
                return 1
            if i>m or j>n:
                return 0
            ans = solve(i+1, j, m, n) + solve(i, j+1, m, n)
            memo[(i,j)] = ans
            return ans
        return solve(0,0,m-1,n-1)
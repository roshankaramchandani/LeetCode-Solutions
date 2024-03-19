class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}
        rows = len(triangle)
        def solve(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            if i==rows-1:
                return triangle[i][j]
            if i==rows:
                return 0
            
            memo[(i,j)] = triangle[i][j] + min(solve(i+1, j), solve(i+1, j+1))
            return memo[(i,j)]
        
        return solve(0,0)
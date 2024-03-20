class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        
        memo = {}
        def solve(row,col1,col2):
            if (row,col1,col2) in memo:
                return memo[(row,col1,col2)]

            curr = grid[row][col1] + grid[row][col2]
            if col1==col2:
                curr = curr//2
            if row==len(grid)-1:
                return curr
            

            nextMax = 0
            for i in range(-1,2):
                if 0<=col1+i<len(grid[0]):
                    for j in range(-1,2):
                        if 0<=col2+j<len(grid[0]):
                            nextMax = max(nextMax, solve(row+1,col1+i,col2+j))
            memo[(row,col1,col2)] = curr + nextMax
            return memo[(row,col1,col2)]
        
        return solve(0,0,len(grid[0])-1)
                
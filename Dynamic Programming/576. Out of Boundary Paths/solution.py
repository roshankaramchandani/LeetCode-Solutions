class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        memo = {}
        def solve(rowpos,colpos,movesleft):
            if (rowpos,colpos,movesleft) in memo:
                return memo[(rowpos,colpos,movesleft)]
            if (rowpos<0 or rowpos>=m) or (colpos<0 or colpos>=n):
                return 1
            if movesleft==0:
                return 0
            
            ans = 0

            ans += solve(rowpos+1,colpos,movesleft-1) % ((10**9)+7)
            ans += solve(rowpos-1,colpos,movesleft-1) % ((10**9)+7)
            ans += solve(rowpos,colpos+1,movesleft-1) % ((10**9)+7)
            ans += solve(rowpos,colpos-1,movesleft-1) % ((10**9)+7)

            memo[(rowpos,colpos,movesleft)] = ans % ((10**9)+7)
            return memo[(rowpos,colpos,movesleft)]
        
        return solve(startRow,startColumn,maxMove)
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        myset = set(stones)
        memo = {}
        def solve(currpos, jump):
            nonlocal myset
            if (currpos,jump) in memo:
                return memo[(currpos,jump)]
            if currpos not in myset:
                return False
            
            if currpos==stones[-1]:
                return True

            ans = False
            nextjumps = [jump-1,jump,jump+1]
            for nextjump in nextjumps:
                if nextjump>0:
                    ans = ans or solve(currpos+nextjump, nextjump)
            memo[(currpos,jump)] = ans
            return memo[(currpos,jump)]
        return solve(1,1)
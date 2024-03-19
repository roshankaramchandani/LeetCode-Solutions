class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def solve(ptr):
            if ptr in memo:
                return memo[ptr]
            if ptr==len(s):
                return True
            if ptr>len(s):
                return False
            
            
            for i in wordDict:
                if s[ptr:].startswith(i):
                    temp = solve(ptr+len(i))
                    if temp:
                        memo[ptr] = temp
                        return True
            memo[ptr] = False
            return False
        
        return solve(0)
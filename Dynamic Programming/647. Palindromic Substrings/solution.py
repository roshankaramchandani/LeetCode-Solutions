class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        def solve(a,b):
            nonlocal ans
            while a>=0 and b<len(s):
               
                if s[a]==s[b]:
                    ans += 1
                else:
                    break
                a -= 1
                b += 1
        
        for i in range(len(s)):
            solve(i,i)
            if i!=len(s)-1:
                solve(i,i+1)
        
        return ans

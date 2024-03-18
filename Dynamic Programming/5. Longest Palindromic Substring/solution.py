class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False]*n for _ in range(n)]

        maxCount = 1
        ans = s[0]

        for i in range(n-1,-1,-1):
            for j in range(n-1,-1,-1):
                if j>=i:
                    if s[i] == s[j]:
                        if j-i<=2:
                            dp[i][j] = True
                        else:
                            dp[i][j] = dp[i+1][j-1]
                if dp[i][j]:
                    if j-i+1>maxCount:
                        maxCount = j-i
                        ans = s[i:j+1]
        return ans
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0]*len(text1) for _ in range(len(text2))]
        for i in range(len(text2)):
            if text1[0] in text2[:i+1]:
                dp[i][0] = 1
        for i in range(len(text1)):
            if text2[0] in text1[:i+1]:
                dp[0][i] = 1
                
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if text2[i] == text1[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        print(dp)
        return dp[-1][-1]
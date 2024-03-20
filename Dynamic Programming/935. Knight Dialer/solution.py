class Solution:
    def knightDialer(self, n: int) -> int:
        if n==1:
            return 10
        dp = [[1]*(n-1) for _ in range(10)]
        jump = {0:[4,6], 1:[6,8], 2:[7,9], 3:[4,8], 4:[0,3,9], 5:[], 6:[0,1,7], 7:[2,6], 8:[1,3], 9:[2,4]}
        
        for i in range(10):
            dp[i][-1] = len(jump[i])
        
        for i in range(n-3,-1,-1):
            for j in range(10):
                jumps = jump[j]
                newAns = 0
                for nextJump in jumps:
                    newAns = (newAns + dp[nextJump][i+1])%((10**9)+7)
                dp[j][i] = newAns

        ans = 0
        for i in range(10):
            ans = (ans + dp[i][0])%((10**9)+7)
        return ans
        

            
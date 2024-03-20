class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        n = len(obstacles)
        dp = [[-1]*n for _ in range(3)]
        
        for level in range(n-1,-1,-1):
            rem = -1
            if level==n-1:
                dp[0][level] = 0
                dp[1][level] = 0
                dp[2][level] = 0
            else:
                for lane in range(1,4):
                    if obstacles[level]==lane:
                        dp[lane-1][level] = math.inf
                    else:
                        if obstacles[level+1]!=lane:
                            dp[lane-1][level] = dp[lane-1][level+1]
                        else:
                            rem = lane
                if rem!=-1:
                    temp = math.inf
                    for lane in range(1,4):
                        if dp[lane-1][level]!=-1:
                            temp = min(temp, dp[lane-1][level])
                    dp[rem-1][level] = 1 + temp
        return dp[1][0]
                



class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n<=3:
            return max(nums)
        
        def robber(arr):
            dp = [0]*len(arr)
            for i in range(len(arr)):
                if i==0:
                    dp[i] = arr[i]
                elif i==1:
                    dp[i] = max(arr[i],dp[i-1])
                else:
                    dp[i] = max(dp[i-1],arr[i] + dp[i-2])
            return dp[-1]
        
        return max(robber(nums[1:]), robber(nums[:-1]))
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False]*len(nums)
        lastTrue = len(nums)-1
        dp[-1] = True
        for i in range(len(nums)-2,-1,-1):
            if nums[i]>=lastTrue-i:
                dp[i] = True
                lastTrue = i
        return dp[0]
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        memo = {}
        def solve(i, left, right):
            if (i,left,right) in memo:
                return memo[(i,left,right)]
            if i==len(multipliers)-1:
                ans = max(nums[left]*multipliers[i],nums[right]*multipliers[i])
                memo[(i,left,right)] = ans
                return ans
            
            
            ans = max((multipliers[i]*nums[left] + solve(i+1,left+1,right)), (multipliers[i]*nums[right] + solve(i+1,left,right-1)))
            memo[(i,left,right)] = ans
            return ans

        return solve(0,0,len(nums)-1)
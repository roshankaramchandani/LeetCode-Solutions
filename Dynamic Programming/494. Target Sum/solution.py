class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def solve(index, curr):
            if (index,curr) in memo:
                return memo[(index,curr)]

            if index==len(nums):
                if curr==target:
                   return 1
                return 0
            
            ans = solve(index+1, curr+nums[index]) + solve(index+1, curr-nums[index])
            memo[(index,curr)] = ans
            return ans
        
        return solve(0,0)
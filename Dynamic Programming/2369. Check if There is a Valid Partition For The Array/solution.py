class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        memo = {}
        def solve(ptr):
            if ptr in memo:
                return memo[ptr]
            if ptr==len(nums):
                return True
            ans = False

            if len(nums)-ptr>=2 and nums[ptr] == nums[ptr+1]:
                ans = ans or solve(ptr+2)
            
            if len(nums)-ptr>=3 and nums[ptr] == nums[ptr+1] == nums[ptr+2]:
                ans = ans or solve(ptr+3)
            if len(nums)-ptr>=3 and nums[ptr]-nums[ptr+1]==nums[ptr+1]-nums[ptr+2]==-1:
                ans = ans or solve(ptr+3)
            
            memo[ptr] = ans
            return memo[ptr]
        
        return solve(0)
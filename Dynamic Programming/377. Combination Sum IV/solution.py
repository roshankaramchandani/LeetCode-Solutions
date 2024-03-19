class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}
        def solve(num):
            if num in memo:
                return memo[num]
            if num<0:
                return 0
            if num==0:
                return 1
            ans = 0
            for i in nums:
                ans += solve(num-i)
            memo[num] = ans
            return memo[num]
        return solve(target)
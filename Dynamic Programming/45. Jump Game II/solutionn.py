class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = {}
        def solve(index):
            if index in memo:
                return memo[index]
            if index==len(nums)-1:
                return 0
            ans = math.inf
            if nums[index]>0:
                for i in range(1,nums[index]+1):
                    if i+index<len(nums):
                        ans = min(ans,1+solve(index+i))
                    else:
                        break
            memo[index]=ans
            return memo[index]
        return solve(0)
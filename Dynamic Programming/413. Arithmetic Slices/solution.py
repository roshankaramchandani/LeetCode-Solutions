class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums)<3:
            return 0
        left = 0
        right = 2
        ans = 0

        while right<len(nums):
            if nums[right]+nums[left] == 2*nums[left+1]:
                ans += 1
                diff = nums[right] - nums[left +1]
                temp = right+1
                while temp<len(nums):
                    if nums[temp]-nums[temp-1] == diff:
                        ans += 1
                        temp += 1
                    else:
                        break

            left += 1
            right += 1
        return ans
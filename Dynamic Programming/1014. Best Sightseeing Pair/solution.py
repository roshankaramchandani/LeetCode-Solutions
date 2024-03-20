class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        curr = 0
        ans = 0
        for i in values:
            ans = max(ans,curr+i)
            curr = max(curr,i) -1
        return ans
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0]*len(nums1) for _ in range(len(nums2))]
        if nums1[0]==nums2[0]:
            dp[0][0] = 1
        
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if i==0:
                    if nums2[i] == nums1[j]:
                        dp[i][j] = 1
                        continue
                    
                if j==0:
                    if nums2[i] == nums1[j]:
                        dp[i][j] = 1
                        continue
                
                if nums2[i] == nums1[j]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                if j==len(dp[0])-1:
                    dp[i][j] = max(max(dp[i]), dp[i-1][j])
        return dp[-1][-1]
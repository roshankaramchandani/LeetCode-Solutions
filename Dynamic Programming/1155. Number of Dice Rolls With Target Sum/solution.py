class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        
        memo = {}
        def solve(n,k,target):

            if (n==1 and target<=k) or (n*k==target) or (n==target):
                return 1
            if n*k<target or target<n:
                return 0
            if (target,n) in memo:
                return memo[(target,n)]
                
            ans = 0
            for i in range(1,k+1):
                if target-i>0:
                    ans += solve(n-1,k,target-i) 
            
            memo[(target,n)] = ans % ((10**9)+7)
            return ans % ((10**9)+7)
        return solve(n,k,target)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def solve(amount):
            if amount in memo:
                return memo[amount]
            if amount == 0:
                return 0
            if amount<0:
                return math.inf
            
            ans = math.inf
            for i in coins:
                ans = min(ans, solve(amount-i))
            memo[amount] = 1+ans
            return 1+ans
        
        ans = solve(amount)
        if math.isinf(ans):
            return -1
        else:
            return ans
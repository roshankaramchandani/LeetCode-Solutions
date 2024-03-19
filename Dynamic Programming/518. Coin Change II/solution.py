class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def solve(currCoin, amount):
            if (currCoin,amount) in memo:
                return memo[(currCoin,amount)]
            if amount==0:
                return 1
            if currCoin>=len(coins):
                return 0
            if amount<0:
                return 0
            memo[(currCoin, amount)] = solve(currCoin, amount-coins[currCoin]) + solve(currCoin+1, amount)
            return memo[(currCoin, amount)]
        return solve(0, amount)
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        memo = {}
        def solve(curr, n):
            if (curr,n) in memo:
                return memo[(curr,n)]
            if n==1:
                return 1
            
            ans = 0
            if curr=="a":
                ans = solve("e", n-1)
            
            if curr=="e":
                ans = solve("a", n-1) + solve("i", n-1)
            
            if curr=="i":
                ans = solve("a", n-1) + solve("e", n-1) + solve("o", n-1) + solve("u", n-1)
            
            if curr=="o":
                ans = solve("i", n-1) + solve("u", n-1)
            
            if curr=="u":
                ans = solve("a", n-1)
            
            memo[(curr,n)] = ans%(10**9 + 7)
            return memo[(curr,n)]
        
        return (solve("a", n) + solve("e", n) + solve("i", n) + solve("o", n) + solve("u", n))%(10**9 + 7)
        
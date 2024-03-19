class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def solve(left):
            if left in memo:
                return memo[left]
            if left==len(s):
                return 1
            if s[left] == "0":
                return 0
            if left==len(s)-1:
                return 1

            oneDigit = solve(left+1)
            memo[left+1] = oneDigit
            twoDigits = 0
            if int(s[left:left+2])<=26:
                twoDigits = solve(left+2)
                memo[left+2] = twoDigits
            return oneDigit+twoDigits
        return solve(0)

            
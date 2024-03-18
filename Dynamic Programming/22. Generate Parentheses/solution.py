class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        stack = []
        def backTrack(openC, closeC):
            if openC == closeC == n:
                ans.append("".join(stack))
                return 0
            
            if openC < n:
                stack.append("(")
                backTrack(openC+1, closeC)
                stack.pop()
            
            if closeC < openC:
                stack.append(")")
                backTrack(openC, closeC+1)
                stack.pop()
        

        backTrack(0,0)
        return ans


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def check(pred, word):
            if len(word)-len(pred)!=1:
                return False
            predptr = 0
            wordptr = 0

            while wordptr<len(word) and predptr<len(pred):
                if word[wordptr] == pred[predptr]:
                    predptr += 1
                wordptr += 1
            if predptr == len(pred):
                return True
            else:
                return False
        
        memo = {}

        def solve(index):
            if index in memo:
                return memo[index]
            
            ans = 1
            for i in range(len(words)):
                if i!=index:
                    if check(words[index], words[i]):
                        ans = max(ans, 1+solve(i))
            memo[index] = ans
            return ans
        
        ans = 0
        for i in range(len(words)):
            ans = max(ans, solve(i))
        return ans
        
       

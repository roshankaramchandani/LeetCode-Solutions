class Solution:
    def addMinimum(self, word: str) -> int:
        ans = 0
        if word[0] == 'b':
            ans += 1
        if word[0] == 'c':
            ans += 2
        if word[-1] == 'b':
            ans += 1
        if word[-1] == 'a':
            ans += 2
        
        
        for i in range(len(word)-1):
            if word[i] == word[i+1]:
                ans += 2
            if word[i] + word[i+1] == 'ac':
                ans += 1
            elif word[i] + word[i+1] == 'ba':
                ans += 1
            elif word[i] + word[i+1] == 'cb':
                ans += 1
        return ans
        
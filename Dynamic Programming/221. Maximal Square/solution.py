class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ans = 0
        rows = len(matrix)
        cols = len(matrix[0])
        
        answer = [[int(matrix[i][j]) for j in range(cols)] for i in range(rows)]
        for i in answer:
            for ele in i:
                if ele==1:
                    ans = 1
        for i in range(rows-2, -1, -1):
            for j in range(cols-1,-1,-1):
                if answer[i][j] == 1:
                    if j<cols-1:
                        answer[i][j] += min(answer[i+1][j], answer[i+1][j+1], answer[i][j+1])
                        ans = max(ans, answer[i][j])
        

        return ans*ans
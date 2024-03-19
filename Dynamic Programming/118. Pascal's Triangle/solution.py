class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1],[1,1]]
        if numRows<=2:
            return ans[:numRows]
        
        for i in range(2,numRows):
            temp = []
            ptr1 = 0
            ptr2 = 1
            temp.append(1)
            while ptr2<len(ans[-1]):
                temp.append(ans[-1][ptr1] + ans[-1][ptr2])
                ptr1 += 1
                ptr2 += 1
            temp.append(1)
            ans.append(temp)
        return ans

        
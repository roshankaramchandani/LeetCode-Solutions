class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        
        ptr = 1
        currMax = 0
        currSum = 0
        ans = 0
        while ptr<len(colors):
            if colors[ptr] == colors[ptr-1]:
                if currMax == 0:
                    currMax = max(neededTime[ptr], neededTime[ptr-1])
                    currSum += neededTime[ptr] + neededTime[ptr-1]
                else:
                    currMax = max(currMax, neededTime[ptr])
                    currSum += neededTime[ptr]
            else:
                ans += currSum-currMax
                currSum = 0
                currMax = 0
            ptr += 1
        
        ans += currSum-currMax
        return ans
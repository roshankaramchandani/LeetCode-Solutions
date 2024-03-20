class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        def solve(used, currSum):
            key = "".join(used)
            if (key,currSum) in memo:
                return memo[(key,currSum)]
            if currSum>=target:
                return currSum
            ans = currSum
            for i in range(len(used)):
                if int(used[i])<2:
                    temp = used.copy()
                    temp[i] = str(int(temp[i])+1)
                    localans = solve(temp, currSum+toppingCosts[i])
                    if abs(target-ans)>abs(target-localans):
                        ans = localans
                    elif abs(target-ans)==abs(target-localans):
                        ans = min(ans,localans)
            memo[(key,currSum)] = ans
            return ans
        memo = {}
        used = ["0"]*len(toppingCosts)
        ans = []
        for i in baseCosts:
            ans.append(solve(used, i))
        
        ret = ans[0]

        for i in ans:
            if i==target:
                return target
            if abs(target-i)<abs(target-ret):
                ret = i
            elif abs(target-i)==abs(target-ret):
                ret = min(i,ret)
        return ret

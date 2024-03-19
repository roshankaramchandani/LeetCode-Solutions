class Solution:
    def numSquares(self, n: int) -> int:
        nums = set()
        start = 1
        while start*start<=n:
            nums.add(start*start)
            start += 1

        dp = [0]*(n+1)
        q = deque()

        q.append(n)
        level = 1
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                for num in nums:
                    newNum = curr-num
                    if newNum==0:
                        return level
                    if newNum>0:
                        q.append(newNum)
            level += 1
        



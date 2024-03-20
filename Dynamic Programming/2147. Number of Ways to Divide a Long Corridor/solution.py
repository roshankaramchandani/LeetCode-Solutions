class Solution:
    def numberOfWays(self, corridor: str) -> int:
        seats = []
        prev = -1
        for i in range(len(corridor)):
            if corridor[i] == "S":
                if prev==-1:
                    prev = i
                else:
                    seats.append((prev,i))
                    prev = -1
        if prev!=-1 or not seats:
            return 0
        ans = 1
        for i in range(1,len(seats)):
            ans = (ans*(seats[i][0]-seats[i-1][1]))%((10**9)+7)
        return ans
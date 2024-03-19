class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2!=0:
            return False
        
        myset = set()
        myset.add(0)
        for i in nums:
            if i==total//2:
                return True
            temp = set()
            for j in myset:
                if i+j==total//2:
                    return True
                temp.add(i)
                temp.add(j+i)
                temp.add(j)
            myset=temp
        return False
class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        numslen = len(nums)
        flag = [0]*(numslen+1)
        flag[0] = 1
        for i in nums:
            flag[i] += 1
        return [flag.index(2),flag.index(0)]
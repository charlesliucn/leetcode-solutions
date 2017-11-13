class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numslen = len(nums)
        flag = [False]*(numslen + 1)
        for i in nums:
            flag[i] = True
        # for f in range(numslen+1):
        #   if flag[f] == False:
        #       return f
        return flag.index(False)